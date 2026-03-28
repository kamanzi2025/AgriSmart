from __future__ import annotations
import hashlib
from typing import Optional
from models import User, UserRole

_users: list[User] = []
_next_id = 1

def _hash(password: str) -> str:
    return hashlib.sha256(
        f"{password}AgriSmartSalt2025".encode()
    ).hexdigest()

def _seed():
    """Pre-load demo accounts."""
    register("Demo Farmer", "+250700000001", "farmer123",
             UserRole.FARMER, "Kigali", "Gisozi")
    register("Extension Officer", "+250700000002", "officer123",
             UserRole.EXTENSION_OFFICER, "Kigali", "HQ")
    register("Admin", "+250700000000", "admin123",
             UserRole.ADMINISTRATOR, "Kigali", "HQ")

def register(full_name, phone, password,
             role=UserRole.FARMER, region="Kigali", village=""):
    """Returns (success: bool, message: str)."""
    global _next_id
    if any(u.phone == phone for u in _users):
        return False, "Phone number already registered."
    _users.append(User(
        user_id=_next_id, full_name=full_name, phone=phone,
        password_hash=_hash(password), role=role,
        region=region, village=village))
    _next_id += 1
    return True, "Registration successful."

def login(phone, password):
    """Returns (success, user_or_None, message)."""
    h = _hash(password)
    user = next((u for u in _users
                 if u.phone == phone and
                    u.password_hash == h and
                    u.is_active), None)
    if user is None:
        return False, None, "Invalid phone number or password."
    return True, user, "Login successful."

_seed()  # runs on import