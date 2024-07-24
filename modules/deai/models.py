# models.py
# 模型上传、版本控制和访问接口
from django.db import models
from django.contrib.auth.models import User

class AIModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ModelVersion(models.Model):
    model = models.ForeignKey(AIModel, on_delete=models.CASCADE, related_name='versions')
    version_number = models.CharField(max_length=50)
    file = models.FileField(upload_to='model_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
# serializers.py
from rest_framework import serializers
from .models import AIModel, ModelVersion

class ModelVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelVersion
        fields = ['id', 'version_number', 'file', 'uploaded_at']

class AIModelSerializer(serializers.ModelSerializer):
    versions = ModelVersionSerializer(many=True, read_only=True)

    class Meta:
        model = AIModel
        fields = ['id', 'name', 'description', 'creator', 'created_at', 'updated_at', 'versions']

# views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import AIModel, ModelVersion
from .serializers import AIModelSerializer, ModelVersionSerializer

class AIModelViewSet(viewsets.ModelViewSet):
    queryset = AIModel.objects.all()
    serializer_class = AIModelSerializer

    @action(detail=True, methods=['post'])
    def upload_version(self, request, pk=None):
        model = self.get_object()
        serializer = ModelVersionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(model=model)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AIModelViewSet

router = DefaultRouter()
router.register(r'models', AIModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
