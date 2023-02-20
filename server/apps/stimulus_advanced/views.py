from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib import messages
import http

from apps.tasks.models import Task
from apps.tasks.forms import TaskForm

# Create your views here.
def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, "Task created successfully")
            return redirect(reverse('stimulus-advanced:task-detail', kwargs={'pk': instance.pk}))
        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        form = TaskForm()
        status = http.HTTPStatus.OK

    return render(request, "stimulus_advanced/create_page.html", {
        'form': form
    }, status=status)

def update_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=instance)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Task updated successfully')
            return redirect(reverse('stimulus-advanced:task-detail', kwargs={'pk': instance.pk}))
        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        status = http.HTTPStatus.OK
        form = TaskForm(instance=instance)

    return render(request, "stimulus_advanced/update_page.html", {
        'form': form
    }, status=status)

def delete_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        instance.delete()
        messages.success(request, 'Task deleted successfully')
        return redirect('stimulus-advanced:task-list')
    
    return render(request, "stimulus_advanced/delete_page.html", {
        'object': instance
    })

def detail_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)

    return render(request, "stimulus_advanced/detail_page.html", {
        'instance': instance
    })

def list_view(request):
    object_list = Task.objects.order_by('-pk')
    return render(request, "stimulus_advanced/list_page.html", {
        'object_list': object_list
    })