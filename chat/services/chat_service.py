import django.contrib.auth

from chat.models import Message, Chat

User = django.contrib.auth.get_user_model()


class ChatService:
    def add_message(self, source_chat, message_author, message_content):
        return Message.objects.create(
            chat=source_chat,
            author=message_author,
            content=message_content
        ).save()

    def get_chat_messages(self, chat):
        return Message.objects.filter(chat=chat)

    def get_chats_of_user(self, user):
        def is_user_in_chat(chat):
            return user in chat.users

        chats = Chat.objects.all()
        return filter(is_user_in_chat, chats.iterator())

    def get_chats_of_user_by_username(self, username):
        self.get_chats_of_user(User.objects.filter(username=username).first())

    def insert_chat_with_users_by_usernames(self, usernames_to_insert):
        chat_record = Chat.objects.create()
        """
        Map all usernames in the `chat_record`, to their corresponding
        `User` records.
        """
        users_to_insert = [User.objects.filter(username=username).first() for
                           username in usernames_to_insert]
        chat_record.users.set(users_to_insert)
        return chat_record

    def insert_chat_with_users(self, users_to_insert):
        chat_record = Chat.objects.create()
        chat_record.users.set(users_to_insert)
        return chat_record
