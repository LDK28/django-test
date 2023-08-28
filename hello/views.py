from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World!')

def about(request):
    return HttpResponse('<h2 style="color:blue;">About our app</h2>')