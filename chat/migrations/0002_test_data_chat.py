import django.contrib.auth
from django.db import migrations, transaction

from chat.resources.chats import CHATS
from chat.services.chat_service import ChatService

User = django.contrib.auth.get_user_model()


class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0001_initial'),
        ('feed', '0008_users'),
    ]

    def generate_chat_records(apps, schema_editor):
        with transaction.atomic():
            chat_service = ChatService()
            for chat in CHATS:
                chat_service.insert_chat_with_users_by_usernames(chat)

    operations = [
        migrations.RunPython(generate_chat_records),
    ]
