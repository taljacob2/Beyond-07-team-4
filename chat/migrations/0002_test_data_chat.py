import django.contrib.auth
from django.db import migrations, transaction

from chat.models import Chat
from chat.resources.chats import CHATS

User = django.contrib.auth.get_user_model()


class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0001_initial'),
        ('feed', '0008_users'),
    ]

    def generate_chat_records(apps, schema_editor):
        with transaction.atomic():
            for chat in CHATS:
                chat_record = Chat.objects.create()
                """
                Map all usernames in the `chat_record`, to their corresponding
                `User` records.
                """
                users = [User.objects.filter(username=username).first() for
                         username in chat]
                chat_record.users.set(users)

    operations = [
        migrations.RunPython(generate_chat_records),
    ]
