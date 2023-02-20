"""task_projects URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('turbo_drive/', include('apps.turbo_drive.urls', namespace='turbo-drive')),
    path('turbo_frame/', include('apps.turbo_frame.urls', namespace='turbo-frame')),
    path('stimulus_basic/', include('apps.stimulus_basic.urls', namespace='stimulus-basic')),
    path('stimulus_advanced/', include('apps.stimulus_advanced.urls', namespace='stimulus-advanced')),
    path('admin/', admin.site.urls),
]
