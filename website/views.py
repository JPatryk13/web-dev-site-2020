from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def hire_me(request):
    return render(request, 'hire_me.html')
