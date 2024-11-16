from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name =models.CharField(max_length=20)
    
    def __str__(self):
        return self.name




class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    body=models.TextField()
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)








