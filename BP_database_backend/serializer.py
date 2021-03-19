from rest_framework.serializers import ModelSerializer
from .models import User, Project


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
