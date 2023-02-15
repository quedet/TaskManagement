import http
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages

from turbo_response import TurboFrame

from apps.tasks.models import Task
from apps.tasks.forms import TaskForm

# Create your views here.
def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Task created Successfully')

            if request.turbo.frame:
                response = TurboFrame(request.turbo.frame).template('turbo_frame/messages.html', {}).response(request)
                return response
            else:
                return redirect(reverse('turbo-frame:task-detail', kwargs={'pk': instance.pk}))
        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        status = http.HTTPStatus.OK
        form = TaskForm()

    return render(request, 'turbo_frame/create_page.html', {
        'form': form
    }, status=status)

def update_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            if request.turbo.frame:
                return redirect(reverse('turbo-frame:task-detail', kwargs={'pk': instance.pk}))
            else:
                messages.success(request, 'Task updated successfully')
                return redirect(reverse('turbo-frame:task-detail', kwargs={'pk': instance.pk}))
        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        status = http.HTTPStatus.OK
        form = TaskForm(instance=instance)

    return render(request, 'turbo_frame/update_page.html', {
        'form': form
    }, status=status)

def delete_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        instance.delete()

        # if request.turbo.frame:
        #     response = TurboFrame(f"task-detail-{instance.pk}").render('')
        #     return response
        # else:
        messages.success(request, 'Task deleted successfully')
        return redirect(reverse('turbo-frame:task-list'))

    return render(request, 'turbo_frame/delete_page.html', {
        'instance': instance
    })

def list_view(request):
    return render(request, 'turbo_frame/list_page.html', {
        'object_list': Task.objects.order_by('-pk')
    })

def detail_view(request, pk):
    instance = get_object_or_404(Task, pk=pk)
    return render(request, 'turbo_frame/detail_page.html', {'instance': instance})

def index_view(request):
    return render(request, 'turbo_frame/index_page.html')