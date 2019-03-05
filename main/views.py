from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def hoodie(request):
    return render(request, 'hoodie.html')

def detail(request):
    return render(request, 'detail.html')

def crewneck(request):
	return render(request, 'crewneck.html')

def pants(request):
	return render(request, 'pants.html')

def outer(request):
	return render(request, 'outer.html')

def accessories(request):
	return render(request, 'accessories.html')
