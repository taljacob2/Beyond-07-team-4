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

            # First user shout-outs a message.
            for chat_record in chats.iterator():
                message_record = Message.objects.create(
                    chat=chat_record,
                    author=chat_record.users.first(),
                    content='Hey! Is anybody here?'
                ).save()

                # Every other user in the chat responds with a message.
                user_index = 0
                for user_record in chat_record.users.iterator():
                    if user_index == 0:
                        continue
                    message_record = Message.objects.create(
                        chat=chat_record,
                        author=user_record,
                        content='I am here!'
                    ).save()
                    user_index += 1

    operations = [
        migrations.RunPython(generate_chat_message_records),
    ]
