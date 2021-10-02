from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination

@api_view(['GET'])
def todoappOverview(request):
    todoapp_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
        'Create' : '/task-new/',
        'Update' : '/task-update/<str:pk>/',
        'Delete' : '/task-delete/<str:pk>/',
    }
    return Response(todoapp_urls)


@api_view(['GET'])
def taskList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 6
    tasks = Task.objects.all().order_by('-id')
    result_page = paginator.paginate_queryset(tasks, request)
    serializer = TaskSerializer(result_page, many=True)

    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)

    return Response(serializer.data)

@api_view(['POST'])
def taskNew(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=tasks, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()

    return Response("Item deleted")