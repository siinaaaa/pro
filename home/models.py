from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Post(models.Model):
    name = models.CharField(max_length=20)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

