from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category
    
class Expenses(models.Model):
    description = models.CharField(max_length=30)
    amount = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.description
    
    @classmethod
    def search_by_description(cls,search_term):
        captions = cls.objects.filter(description__icontains=search_term)
        return captions