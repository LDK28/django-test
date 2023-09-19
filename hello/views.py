from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('<h2 style="color:blue;">About our app</h2>')

def dude(request, name):
    langs = ["Russian", "English", "French"]
    data = {"name": name, "langs": langs, "showButton": False}
    return render(request, 'dude.html', context=data)