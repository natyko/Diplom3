import random
import string
import uuid
import requests
from config import API_URL


def generate_random_email():
    """Generate a random email for testing."""
    username = "".join(random.choices(string.ascii_lowercase + string.digits, k=10))
    domain = "".join(random.choices(string.ascii_lowercase, k=7))
    return f"{username}@{domain}.com"


def generate_test_user():
    """Generate a test user with unique email."""
    return {
        "email": f"test_{uuid.uuid4()}@yandex.ru",
        "password": "123456",
        "name": "Test User"
    }


def register_user(user):
    """Register a user via the API."""
    response = requests.post(f"{API_URL}/auth/register", json=user)
    response.raise_for_status()
    return response