from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

import http

from apps.tasks.models import Task
from apps.tasks.forms import TaskForm

# Create your views here.
def counter_view(request):
    return render(request, 'stimulus_basic/counter.html')

def create_view(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task created successfully!")
            return redirect(reverse('stimulus-basic:task-list'))
        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        form = TaskForm()
        status = http.HTTPStatus.OK
    return render(request, "stimulus_basic/create_page.html", {
        'form': form
    }, status=status)

def list_view(request):
    object_list = Task.objects.order_by('-pk')
    return render(request, "stimulus_basic/list_page.html", {
        'object_list': object_list
    })

def update_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Task Updated successfully!")
            return redirect(reverse('stimulus-basic:task-list'))
        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        form = TaskForm(instance=instance)
        status = http.HTTPStatus.OK
    return render(request, "stimulus_basic/update_page.html", {
        'form': form
    }, status=status)

def delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        task.delete()
    return render(request, "stimulus_basic/delete_page.html", {

    })
