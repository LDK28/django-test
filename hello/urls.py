from django.urls import path
from hello.views import index, about, dude

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('dude/<str:name>', dude, name='dude'),
]
