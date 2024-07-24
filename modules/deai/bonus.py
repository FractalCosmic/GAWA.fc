# models.py
# 基于贡献度计算算法进行贡献激励
class UserContribution(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.ForeignKey(AIModel, on_delete=models.CASCADE)
    contribution_score = models.FloatField(default=0)
    sg_tokens = models.FloatField(default=0)

# tasks.py
from django.db.models import Sum

@shared_task
def calculate_contributions():
    for model in AIModel.objects.all():
        total_accuracy = model.versions.aggregate(Sum('evaluations__accuracy'))['evaluations__accuracy__sum'] or 0
        total_f1 = model.versions.aggregate(Sum('evaluations__f1_score'))['evaluations__f1_score__sum'] or 0
        
        contribution_score = total_accuracy + total_f1
        
        UserContribution.objects.update_or_create(
            user=model.creator,
            model=model,
            defaults={'contribution_score': contribution_score}
        )

@shared_task
def distribute_sg_tokens():
    total_contribution = UserContribution.objects.aggregate(Sum('contribution_score'))['contribution_score__sum'] or 1
    total_sg_tokens = 1000  # 假设每个计算周期分发1000个SG代币
    
    for contribution in UserContribution.objects.all():
        sg_tokens = (contribution.contribution_score / total_contribution) * total_sg_tokens
        contribution.sg_tokens += sg_tokens
        contribution.save()

# views.py
class UserContributionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = UserContribution.objects.all()
    serializer_class = UserContributionSerializer

    def list(self, request):
        contributions = self.queryset.filter(user=request.user)
        serializer = self.get_serializer(contributions, many=True)
        return Response(serializer.data)
