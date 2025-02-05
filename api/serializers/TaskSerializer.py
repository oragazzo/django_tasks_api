from rest_framework import serializers
from api.models.Task import Task

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ('id', 'task', 'completed', 'created_at')