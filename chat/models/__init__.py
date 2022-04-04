"""
ATTENTION:
The following imports are mandatory for running:
```
pipenv run python manage.py makemigrations chat
```
"""

from .chat import Chat
from .message import Message
from .user_chat import UserChat
