from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Counter
# Create your views here.
def home(request):
    c = Counter.objects.all().first()
    count = c.count
    data = {
        'count' : count
    } 
    return render(request, 'home.html', context=data)

def increment(request):
    c = Counter.objects.all().first()
    c.count = c.count + 1
    c.save()
    return redirect('home')

def decrement(request):
    c = Counter.objects.all().first()
    c.count = c.count - 1
    if c.count < 0:
        c.count =0
    c.save()
    return redirect('home')

def reset(request):
    c = Counter.objects.all().first()
    c.count = 0
    c.save()
    return redirect('home')