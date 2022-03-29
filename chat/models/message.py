from django.db import models


class Message(models.Model):
    # chat_id  # TODO: Add later.
    # author_id  # TODO: Add later.
    date_posted = models.DateTimeField(auto_now_add=True)
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
