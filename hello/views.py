from django.http import HttpResponse
from django.shortcuts import render

from .models import TestModel

from .forms import UserForm

def index(request):
    data = TestModel.objects.all()
    context = {"data": data}
    return render(request, 'index.html', context=context)

def about(request):
    return HttpResponse('<h2 style="color:blue;">About our app</h2>')

def dude(request, name):
    langs = ["Russian", "English", "French"]
    data = {"name": name, "langs": langs, "showButton": False}
    return render(request, 'dude.html', context=data)

def signin(request):
    if request.method == 'POST':
        userform = UserForm(request.POST)
        if userform.is_valid():
            email = userform.cleaned_data["email"]
            return render(request, 'signin.html', context={"email": email})
        
    userform = UserForm()
    return render(request, 'signin.html', context={"form": userform})