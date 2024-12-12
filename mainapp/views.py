from django.shortcuts import render
from .models import ToDo

def index(request):
    return render(request, 'index.html')

def todolist(request):
    todos = ToDo.objects.all()
    context = {'todos': todos}
    return render(request, 'todolist.html', context=context)
