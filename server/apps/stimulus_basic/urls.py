from django.urls import path
from apps.stimulus_basic import views

app_name = 'stimulus-basic'

urlpatterns = [
    path('counter/', views.counter_view, name='counter'),
    # path('turbo_frame_load/', views.turbo_frame_load_view, name='turbo_frame_load'),
    path('list/', views.list_view, name='task-list'),
    path('create/', views.create_view, name='task-create')
]