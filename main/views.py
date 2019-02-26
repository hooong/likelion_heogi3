from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def hoodie(request):
    return render(request, 'hoodie.html')

def detail(request):
    return render(request, 'detail.html')
