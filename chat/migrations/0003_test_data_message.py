import django.contrib.auth
from django.db import migrations, transaction

from chat.services.chat_test_service import ChatTestService

User = django.contrib.auth.get_user_model()


class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0002_test_data_chat'),
    ]

    def generate_chat_message_records(apps, schema_editor):
        with transaction.atomic():
            chat_test_service = ChatTestService()
            chat_test_service.test_insert_messages_for_each_user_in_each_chat()

    operations = [
        migrations.RunPython(generate_chat_message_records),
    ]
