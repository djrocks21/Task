

from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=100) 
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    

    class Meta:
        db_table = 'User'



class Post(models.Model):
    text = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_constraint=False)   #db_constraint=False -- Database on only Model level




    class Meta:
        db_table = 'Post'
















































