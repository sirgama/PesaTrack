from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category