# models.py
class Review(models.Model):
    research = models.ForeignKey(Research, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    score = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 star rating
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('research', 'reviewer')  # Ensure one review per research per reviewer

# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Research, Review
from .forms import ReviewForm

def submit_review(request, research_id):
    research = get_object_or_404(Research, id=research_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.research = research
            review.reviewer = request.user
            review.save()
            return redirect('research_detail', research_id=research.id)
    else:
        form = ReviewForm()
    return render(request, 'submit_review.html', {'form': form, 'research': research})

def research_detail(request, research_id):
    research = get_object_or_404(Research, id=research_id)
    reviews = research.reviews.all()
    return render(request, 'research_detail.html', {'research': research, 'reviews': reviews})
