from django.shortcuts import render, redirect
from .models import Todo


def index(request):
    todos = Todo.objects.order_by("completed")
    context = {"todos": todos}
    return render(request, "todolist/index2.html", context)


def completeTodo(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.completed = not todo.completed  # Toggle the completed status
    todo.save()
    return redirect("index")
