from django.shortcuts import render

from rest_framework import viewsets
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer
from .permissions import IsOwner
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only show categories belonging to the logged-in user
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the user when a category is created
        serializer.save(user=self.request.user)



class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filterset_fields = ['status', 'priority', 'due_date']
    ordering_fields = ['due_date', 'priority']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['patch'])
    def toggle_status(self, request, pk=None):
        task = self.get_object()
        task.status = 'Completed' if task.status == 'Pending' else 'Pending'
        task.save()
        return Response(
            {"message": "Task status updated."},
            status=status.HTTP_200_OK
        )
