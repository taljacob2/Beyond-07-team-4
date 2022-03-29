from django.db import models


class Message(models.Model):
    # chat_id  # TODO: Add later.
    # author_id  # TODO: Add later.
    date_posted = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
