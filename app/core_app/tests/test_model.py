from django.test import TestCase
from django.contrib.auth import get_user_model






class ModelTests(TestCase):

# Test that creating a new user with an email is successful
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test0@example.com'
        user = get_user_model().objects.create_user(
            email=email,
            password='testpass123')
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password('testpass123'))


# Check that the email is normalized when creating a new user
    def test_email_normalized(self):
        """Test the email for a new user is normalized"""
        sample_emails=[
            ['test1@example.com', 'test1@example.com'],
            ['Test2@EXAMPLE.COM','test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'test3@example.com']
        ]    
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'test123')
            self.assertEqual(user.email, expected)

# Check that creating a user without an email raises a ValueError
    def test_new_user_without_email_raises_error(self):
        """Test creating a user without an email raises a ValueError"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'test123')

# check that creating a new superuser is successful 
    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test_superuser@example.com',
            'test123'
        )
        self.assertEqual(user.email, 'test_superuser@example.com')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)