from django.contrib.auth.models import User
from django.db import models

from .chat import Chat


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, blank=True, null=True)

    # TODO:
    """
    Consult with Omer:
    That on COMMENT and POST, the FK to the author should be:
    
    ```
    author = models.ForeignKey(User, blank=True, null=True)
    ```
    """
    date_posted = models.DateTimeField(
        auto_now_add=True)  # TODO: Change to: `models.DateTimeField(default=timezone.now)`
    content = models.TextField()

    def __str__(self):
        """
        :return: First characters in the `content` string.
        In case `content` is `None`, return `self.id` instead.
        """
        if self.content is not None:
            return str(f'{self.content[0:40]}...')
        else:
            return self.id
