from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from apps.tasks.forms import TaskForm
from apps.tasks.models import Task

import http

# Create your views here.
def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save()
            messages.success(request, 'Task created successfully')
            return redirect(reverse('turbo-drive:list'))
        status = http.HTTPStatus.UNPROCESSABLE_ENTITY
    else:
        form = TaskForm()
        status = http.HTTPStatus.OK
    return render(request, 'turbo_drive/create.html', {
        'form': form
    }, status=status)

def list_view(request):
    import time
    time.sleep(2)
    return render(request, 'turbo_drive/list.html', {
        'object_list': Task.objects.order_by('-pk')
    })
