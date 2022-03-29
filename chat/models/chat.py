from django.db import models


class Chat(models.Model):
    def __str__(self):
        return str(self.id)

    pass
