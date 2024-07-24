# models.py
# 模型评估和排名系统
class ModelEvaluation(models.Model):
    model_version = models.ForeignKey(ModelVersion, on_delete=models.CASCADE, related_name='evaluations')
    accuracy = models.FloatField()
    f1_score = models.FloatField()
    evaluated_at = models.DateTimeField(auto_now_add=True)

# tasks.py
from celery import shared_task
from .models import ModelVersion, ModelEvaluation
import joblib
from sklearn.metrics import accuracy_score, f1_score

@shared_task
def evaluate_model(version_id):
    version = ModelVersion.objects.get(id=version_id)
    model = joblib.load(version.file.path)
    
    # 这里应该是你的评估数据集和标签
    X_test, y_test = load_test_data()
    
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    
    ModelEvaluation.objects.create(
        model_version=version,
        accuracy=accuracy,
        f1_score=f1
    )

# views.py
from django.db.models import Avg

class AIModelViewSet(viewsets.ModelViewSet):
    # ...

    @action(detail=False, methods=['get'])
    def rankings(self, request):
        rankings = AIModel.objects.annotate(
            avg_accuracy=Avg('versions__evaluations__accuracy'),
            avg_f1=Avg('versions__evaluations__f1_score')
        ).order_by('-avg_accuracy', '-avg_f1')
        serializer = self.get_serializer(rankings, many=True)
        return Response(serializer.data)
