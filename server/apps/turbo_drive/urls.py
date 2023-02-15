from django.urls import path
from apps.turbo_drive import views

app_name = 'turbo-drive'

urlpatterns = [
    path('list/', views.list_view, name='list'),
    path('create/', views.create_view, name='create')
]