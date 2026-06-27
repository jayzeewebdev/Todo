from django.contrib import admin
from django.urls import include, path

from Todo_App import views

urlpatterns = [
    path('', views.homepage, name='home'),
]
