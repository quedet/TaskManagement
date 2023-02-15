from django.urls import path
from apps.stimulus_basic import views

app_name = 'stimulus-basic'

urlpatterns = [
    path('counter/', views.counter_view, name='counter')
]