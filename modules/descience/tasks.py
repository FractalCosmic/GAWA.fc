# tasks.py
from celery import shared_task
from .models import Research, Review, UserProfile
from django.db.models import Avg, Count

@shared_task
def calculate_contributions():
    # Calculate research contributions
    researches = Research.objects.annotate(
        avg_score=Avg('reviews__score'),
        review_count=Count('reviews')
    )
    
    for research in researches:
        contribution = research.avg_score * (1 + research.review_count / 10)  # Example formula
        author_profile = UserProfile.objects.get(user=research.author)
        author_profile.contribution_score += contribution
        author_profile.save()
    
    # Calculate review contributions
    reviews = Review.objects.all()
    for review in reviews:
        contribution = review.score * 0.1  # Example formula
        reviewer_profile = UserProfile.objects.get(user=review.reviewer)
        reviewer_profile.contribution_score += contribution
        reviewer_profile.save()

@shared_task
def distribute_sg_tokens():
    total_contribution = UserProfile.objects.aggregate(total=Sum('contribution_score'))['total']
    total_sg_tokens = 1000  # Example: 1000 SG tokens to distribute

    for profile in UserProfile.objects.all():
        sg_tokens = (profile.contribution_score / total_contribution) * total_sg_tokens
        profile.sg_balance += sg_tokens
        profile.contribution_score = 0  # Reset contribution score
        profile.save()

# models.py
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contribution_score = models.FloatField(default=0)
    sg_balance = models.FloatField(default=0)

# views.py
from django.contrib.auth.decorators import login_required

@login_required
def user_dashboard(request):
    profile = request.user.userprofile
    return render(request, 'user_dashboard.html', {'profile': profile})
