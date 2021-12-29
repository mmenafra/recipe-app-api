from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models

def sample_user(email='test@london.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)
class ModelTests(TestCase):
    
    def test_create_user_with_email_successfull(self):
        email = "test@gmail.com"
        pwd = 'Test12345&32cds'

        user = get_user_model().objects.create_user(
            email=email,
            password=pwd
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(pwd))
    
    def test_new_user_email_normalized(self):
        email = 'test@LONDON.COM'

        user = get_user_model().objects.create_user(
            email=email,
            password='Test12345'
        )

        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_superuser(None, 'test123')

    def test_create_new_super_user(self):
        user = get_user_model().objects.create_superuser(
            email='email@fdre.com',
            password='64783645832'
        )

        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_tag_str(self):
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='Vegan'
        )

        self.assertEqual(str(tag), tag.name)
