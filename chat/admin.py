from django.contrib import admin

from chat.models.chat import Chat
from chat.models.message import Message

admin.site.register(Chat)
admin.site.register(Message)
