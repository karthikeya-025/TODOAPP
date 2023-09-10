from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    forms = TaskForm()
    if request.method == "POST":
        forms = TaskForm(request.POST)
        if forms.is_valid():
            forms.save()
        return redirect("/")
    context = {"tasks": tasks, "forms": forms}
    return render(request, "to_do/list.html", context)


def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("/")

    context = {"form": form}
    return render(request, "to_do/update_list.html", context)


def delete(request, pk):
    task = Task.objects.get(id=pk)
    context = {"item": task}
    if request.method == "POST":
        task.delete()
        return redirect("/")
    return render(request, "to_do/delete.html", context)
