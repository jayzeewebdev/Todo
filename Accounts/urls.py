from django.urls import path

from Accounts import views

urlpatterns = [
  path('register/', views.register, name='register'),
  path('login/', views.login_view, name='login'),
]