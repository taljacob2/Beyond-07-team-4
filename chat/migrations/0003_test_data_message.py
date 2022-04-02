import django.contrib.auth
from django.db import migrations, transaction

from chat.models import *

User = django.contrib.auth.get_user_model()


class Migration(migrations.Migration):
    dependencies = [
        ('chat', '0002_test_data_chat'),
    ]

    def generate_chat_message_records(apps, schema_editor):
        with transaction.atomic():
            chats = Chat.objects.all()

            """
            For each chat record, the first user in the chat shout-outs a 
            message. Afterwards, every other user in the chat responds with a 
            message.
            """
            for chat_record in chats.iterator():
                message_record = Message.objects.create()
                message_record.chat = chat_record
                message_record.author = chat_record.users.first()
                message_record.content = 'Hey! Is anybody here?'

                for user_index in range(1, len(chat_record.users.iterator())):
                    message_record = Message.objects.create()
                    message_record.chat = chat_record
                    message_record.author = chat_record.users[user_index]
                    message_record.content = 'I am here!'

    operations = [
        migrations.RunPython(generate_chat_message_records),
    ]
