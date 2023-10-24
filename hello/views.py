from django.http import HttpResponse
from django.shortcuts import render

from .forms import UserForm

def index(request):
    return render(request, 'index.html')

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