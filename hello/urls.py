from django.urls import path
from hello.views import index, about, dude, signin

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('signin/', signin, name='about'),
    path('dude/<str:name>', dude, name='dude'),
]
