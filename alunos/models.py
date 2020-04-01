from django.contrib.auth.models import User
from django.db import models


class Aluno(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.user.username
