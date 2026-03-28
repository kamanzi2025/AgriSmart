from __future__ import annotations
from typing import Optional
from models import User

# the currently authenticated user
current_user: Optional[User] = None

def set_user(user: User):
    global current_user
    current_user = user

def clear():
    """Called on logout."""
    global current_user
    current_user = None

def user_id() -> int:
    return current_user.user_id if current_user else 0