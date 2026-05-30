from django.contrib import admin

from TodoApp.models import Task

#Modifying the admin site in the backend
class TaskAdmin(admin.ModelAdmin):
  list_display = ['title', 'is_complete', 'created_at']

# Register your models here.
admin.site.register(Task, TaskAdmin)