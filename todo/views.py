from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Task


def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    #return HttpResponse('the form is submitted')
    return redirect('home')
