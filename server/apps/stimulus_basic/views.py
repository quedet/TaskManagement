from django.shortcuts import render

# Create your views here.
def counter_view(request):
    return render(request, 'stimulus_basic/counter.html')