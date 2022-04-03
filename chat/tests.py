import django.contrib.auth
import pytest

from chat.models import Chat, Message
from chat.services.chat_service import ChatService
from chat.services.chat_test_service import ChatTestService, \
    TEST_FIRST_USER_MESSAGE_CONTENT, TEST_OTHER_USERS_MESSAGE_CONTENT

User = django.contrib.auth.get_user_model()


def test_chat_app_entrypoint(client):
    response = client.get("/chat/")
    assert response.status_code == 200

@pytest.fixture
def create_users(db):
    user0 = User.objects.create_user('user0', password='123123')
    assert User.objects.filter(username='user0').exists()
    user1 = User.objects.create_user('user1', password='123345')
    assert User.objects.filter(username='user1').exists()
    user2 = User.objects.create_user('user2', password='123678')
    assert User.objects.filter(username='user2').exists()
    user3 = User.objects.create_user('user3', password='123321')
    assert User.objects.filter(username='user3').exists()
    print(User.objects.all())
    return [user0, user1, user2, user3]


@pytest.fixture
def create_chats(db, create_users):
    chat_service = ChatService()
    chat0 = chat_service.insert_chat_with_users(create_users[0:1])
    chat1 = chat_service.insert_chat_with_users(create_users[0:2])
    chat2 = chat_service.insert_chat_with_users(create_users[0:3])
    chat3 = chat_service.insert_chat_with_users(create_users[1:4])
    chat4 = chat_service.insert_chat_with_users(create_users)
    return [chat0, chat1, chat2, chat3, chat4]


@pytest.fixture
def create_data_records():
    chat_test_service = ChatTestService()
    chat_test_service.test_insert_messages_for_each_user_in_each_chat()
    return Chat.objects.all()


@pytest.mark.usefixtures("create_data_records")
@pytest.mark.usefixtures("create_chats")
@pytest.mark.django_db
class TestRecords:
    def test_data_existence(self):
        chat_service = ChatService()

        assert Message.objects.filter(
            content=TEST_FIRST_USER_MESSAGE_CONTENT).exists()

        assert Message.objects.filter(
            content=TEST_OTHER_USERS_MESSAGE_CONTENT).exists()

        print(Chat.objects.all())  # DE-BUG
        chats_of_user1 = chat_service.get_chats_of_user_by_username('user1')
        print(chats_of_user1)  # DE-BUG
        assert chats_of_user1 is not None

        chat_service.add_message(chats_of_user1[0], User.objects.filter(
            username='user1').first(), 'Hello!')
        assert chat_service.get_chat_messages(chats_of_user1[0]).filter(
            content='Hello!').exists()

    def test_data_deletion(self, create_data_records):
        for chat in create_data_records:
            chat.delete()
            assert chat not in Chat.objects.all()
