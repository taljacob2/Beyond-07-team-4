from chat.resources.chats import CHATS
from django.db import migrations

from chat.models import Chat

import django.contrib.auth
User = django.contrib.auth.get_user_model()


class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0001_initial'),
        ('feed', '0008_users'),
    ]

    def generate_chat_data(apps, schema_editor):
        for chat in CHATS:
            # Map all usernames in the `chat`, to their corresponding `User` records.
            users = [User.objects.filter(username=username).first() for
                     username in chat]
            Chat(users=users).save()

    operations = [
        migrations.RunPython(generate_chat_data),
    ]
