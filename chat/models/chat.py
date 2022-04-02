from django.contrib.auth.models import User
from django.db import models


class Chat(models.Model):
    users = models.ManyToManyField(User, related_name="users")

    def __str__(self):
        """
        :return: First usernames of all the users' names that participate in
        this chat".
        In case `self.users` is `None` ( = there are no users who participate
        in this chat), return `self.id` instead.
        """
        user_limit_to_present = 10

        if self.users is not None:

            # Get the usernames of all users that participate in this chat.
            user_names = [user.username for user in self.users.iterator()]
            return str(f'{user_names[0:user_limit_to_present]}...') if len(
                user_names) > user_limit_to_present else str(user_names)
        else:
            return self.id
