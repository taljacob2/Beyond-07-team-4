from chat.models import Chat, Message

TEST_FIRST_USER_MESSAGE_CONTENT = 'Hey! Is anybody here?'
TEST_OTHER_USERS_MESSAGE_CONTENT = 'I am here!'


class ChatTestService:

    def test_insert_messages_for_each_user_in_each_chat(self):
        """
        For each chat record, the first user in the chat shout-outs a
        message. Afterwards, every other user in the chat responds with a
        message.
        """

        # First user shout-outs a message.
        chats = Chat.objects.all()
        for chat_record in chats.iterator():
            Message.objects.create(
                chat=chat_record,
                author=chat_record.users.first(),
                content=TEST_FIRST_USER_MESSAGE_CONTENT
            ).save()

            # Every other user in the chat responds with a message.
            user_index = -1
            for user_record in chat_record.users.iterator():
                user_index += 1
                if user_index == 0:
                    continue
                Message.objects.create(
                    chat=chat_record,
                    author=user_record,
                    content=TEST_OTHER_USERS_MESSAGE_CONTENT
                ).save()
