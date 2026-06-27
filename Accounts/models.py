from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):

  first_name = models.CharField(max_length=50, default=None)
  last_name = models.CharField(max_length=50, default=None)
  date_of_birth = models.DateField()
  contact_number = models.CharField(max_length=15)
  email = models.EmailField(unique=True, blank=False, null=False)
  profile_pic = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True, null=True)
  password = models.CharField(max_length=128)
  confirm_password = models.CharField(max_length=128)
  bio = models.TextField(max_length=1000)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.first_name

  class Meta:
    verbose_name_plural = 'Profile'
