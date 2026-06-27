from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from Accounts.forms import ProfileForm

# Create your views here.

def register(request):
  form = ProfileForm()

  if request.method == 'POST':
    form = ProfileForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()

  context = {
    'form': form,
  }    
  return render (request, 'Accounts/register.html', context)

def login_view(request):
  form = AuthenticationForm()

  if request.method == 'POST':
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')

      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)

  context = {
    'form': form,
  }    
  return render(request, 'Accounts/login.html', context)