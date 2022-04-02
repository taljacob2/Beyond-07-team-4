from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from .chat import Chat


class Message(models.Model):
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    # TODO:
    """
    Consult with Omer:
    That on COMMENT and POST, the FK to the author should be:
    
    ```
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    ```
    """
    date_posted = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    def __str__(self):
        """
        :return: First characters in the `self.content` string.
        In case `self.content` is `None`, return `self.id` instead.
        """
        character_limit_to_present = 40

        if self.content is not None:
            content_str = str(
                f'{self.content[0:character_limit_to_present]}...') if len(
                self.content) > character_limit_to_present else str(
                self.content)
            username = self.author.username if self.author is not None else 'Deleted User'
            return f'{username}: {content_str}'
        else:
            return self.id
