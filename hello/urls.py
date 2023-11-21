from django.urls import path, include
from hello.views import index, about, dude, signin

from rest_framework import routers

from hello import api

test_api = routers.DefaultRouter()
test_api.register('test', api.TestApi, basename='test_api')

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('signin/', signin, name='about'),
    path('dude/<str:name>', dude, name='dude'),
    path('api/', include(test_api.urls))
]
