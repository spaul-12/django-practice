from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
@api_view(['GET'])
def apioverview(request):
    api_urls={
        'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def tasklist(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskdetail(request,pk):
    task=Task.objects.get(id=pk)
    serializer = TaskSerializer(task)
    return Response(serializer.data)


@api_view(['POST','GET'])
def taskupdate(request,pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task,data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)    

@api_view(['POST'])
def createtask(request):
    serializer=TaskSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)    


@api_view(['DELETE'])
def deltask(request,pk):
    task=Task.objects.get(id=pk)
    task.delete()
    return Response("Item deleted")