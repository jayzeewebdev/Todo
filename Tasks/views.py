from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def add_task(request):
  return HttpResponse('add tasks from here!')