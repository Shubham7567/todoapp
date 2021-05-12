import re
from django.http import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer


@api_view(['GET','POST'])
def task_list(request):
    if request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks,many=True)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def task_detail(request,id):
    task = Task.objects.get(id=id)
    if request.method == "GET":
        serializer = TaskSerializer(task,many=False)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == "PUT":
        serializer = TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)