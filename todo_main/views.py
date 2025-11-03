from django.shortcuts import render
from todo.models import Task

def home(request):

   
    return render(request,'home.html',{
            "tasks" : Task.objects.filter(is_completed=False).order_by('-updated_at'),
            'completed_tasks':Task.objects.filter(is_completed=True),

    })