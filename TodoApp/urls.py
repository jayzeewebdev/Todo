from django.urls import path
from . import views


urlpatterns = [
  path('home/', views.home, name='HomePage'),
  path('task_add/', views.task_add, name='task_add'),
  path('form/', views.form),
]