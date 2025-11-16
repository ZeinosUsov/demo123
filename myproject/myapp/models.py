from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fio = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.fio


class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, default='new')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title