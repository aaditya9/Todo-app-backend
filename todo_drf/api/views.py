from django.shortcuts import render
from  django.http import JsonResponse

from  rest_framework.decorators import api_view
from rest_framework.response import Response
from  .serializers import TaskSerializer
from .models import Task
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'list':'/task-list/',
        'details':'/task-detail/<str:pk>/',
        'create':'/task-create/',
        'update':'/task-update/<str:pk>/',
        'delete':'/task-delete/<str:pk>/',
    }
    return Response(api_urls)
    # return JsonResponse("Api Base point",safe=False)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all()
    # print(tasks)
    serializer = TaskSerializer(tasks,many=True)
    # print(serializer.data)
    result = Response(serializer.data)
    print(result)
    return Response(serializer.data)



@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id=pk)
    print(tasks)
    serializer = TaskSerializer(tasks,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def taskCreate(request,):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request,pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=tasks,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def taskDelete(request,pk):
    tasks = Task.objects.get(id=pk)
    tasks.delete()
    return Response("Task deleted succesfully !!")