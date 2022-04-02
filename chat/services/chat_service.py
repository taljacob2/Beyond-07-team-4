import django.contrib.auth

from chat.models import Message, Chat

User = django.contrib.auth.get_user_model()


class ChatService:
    def add_message(self, source_chat, message_author, message_content):
        Message.objects.create(
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
        self.get_chats_of_user(User.object.filter(username=username).first())
