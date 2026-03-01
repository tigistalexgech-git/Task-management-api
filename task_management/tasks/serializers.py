from rest_framework import serializers
from .models import Task, Category
from django.utils import timezone

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =['url', 'id', 'title', 'description', 'due_date', 'priority', 'status', 'category'] 
        read_only_fields = ['user', 'completed_at']

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user', 'completed_at']

    def validate_due_date(self, value):
        if value <= timezone.now():
            raise serializers.ValidationError("Due date must be in the future.")
        return value

    def update(self, instance, validated_data):
        if instance.status == 'Completed':
            raise serializers.ValidationError(
                "Completed tasks cannot be edited unless reverted to Pending."
            )
        return super().update(instance, validated_data)