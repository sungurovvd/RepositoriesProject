from django.db import models
from django.contrib.auth.models import User


class Repository(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    subs = models.ManyToManyField(User)


class Package(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    content = models.TextField()




# Create your models here.
