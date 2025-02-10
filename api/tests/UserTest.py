from django.test import TestCase
from django.contrib.auth.models import User

# Create your tests here.

class TestUser(TestCase):
    def test_user_creation(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        self.assertEqual(user.username, "testuser")
        self.assertTrue(user.check_password("testpassword"))

    def test_user_creation_with_email(self):
        user = User.objects.create_user(username="testuser", password="testpassword", email="test@example.com")
        self.assertEqual(user.email, "test@example.com")

    def test_user_creation_with_empty_username(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(username="", password="testpassword")

    def test_user_creation_with_empty_password(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(username="testuser", password="")