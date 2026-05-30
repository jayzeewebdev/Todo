from django.http import HttpResponse
from django.shortcuts import redirect, render
from TodoApp.models import Task

# Create your views here.
def home(request):
  tasks = Task.objects.all()
  context = {
    'tasks': tasks
  }
  return render (request, 'home.html', context)

def task_add(request):
    if request.method == 'POST':
       title = request.POST.get('title')
       if title:
          Task.objects.create(title=title)
    return redirect('HomePage')

def form(request):
  return render(request, 'form.html')