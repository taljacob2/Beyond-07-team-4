from django.db import models


# TODO: Check if required.
class UserChat(models.Model):
    # chat_id  # TODO: Add later.
    # author_id  # TODO: Add later.

    def __str__(self):
        return str(self.id)

    pass
