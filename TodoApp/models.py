from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=200)
  description = models.TextField(max_length=5000)
  is_complete = models.BooleanField(default=False)
  created_at = models.DateField(default=timezone.now)
  updated_at = models.DateField(auto_now=True)

  def __str__(self):
    return self.title
  