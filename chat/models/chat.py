from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    users = models.ManyToManyField(User, related_name="users")

    def __str__(self):
        return str(self.id)

    pass
