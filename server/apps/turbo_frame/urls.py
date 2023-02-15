from django.urls import path
from apps.turbo_frame import views

app_name = 'turbo-frame'

urlpatterns = [
    path('', views.index_view, name='index'),
    path('list/', views.list_view, name='task-list'),
    path('create/', views.create_view, name='task-create'),
    path('<int:pk>/', views.detail_view, name='task-detail'),
    path('<int:pk>/update/', views.update_view, name='task-update'),
    path('<int:pk>/delete/', views.delete_view, name='task-delete')
]