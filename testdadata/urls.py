from django.urls import path

from .views import *


urlpatterns = [
    path('', hello, name='home'),
    path('admin/testdadata/dadata/add/', hello, name='home'),
    path('admin/testdadata/dadata/', index, name='dadata'),
]
