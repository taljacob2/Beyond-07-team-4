from django.contrib import admin

from chat.models.chat import Chat
from chat.models.message import Message
from chat.models.user_chat import UserChat

admin.site.register(Chat)
admin.site.register(Message)
admin.site.register(UserChat)
