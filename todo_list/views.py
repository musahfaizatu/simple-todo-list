from django.shortcuts import render, redirect
from .models import Todo
from .form import TodoForm
from django.contrib import messages
from django.http import JsonResponse


def home(request):
    if request.method == 'POST':
        form = TodoForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_todos = Todo.objects.all()
            return render(request, 'todo.html', {'all_todos':all_todos})

    else:
        all_todos = Todo.objects.all()
        return render(request, 'todo.html', {'all_todos':all_todos})

def delete(request, activity_id):
    activity = Todo.objects.get(pk=activity_id)
    activity.delete()
    messages.success(request, ('Activity deleted!!'))
    return redirect('home')
