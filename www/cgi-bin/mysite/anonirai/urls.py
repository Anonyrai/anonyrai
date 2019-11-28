from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('anonirai', views.anonirai, name='anonirai'),
    path('result', views.result, name='result')
]
