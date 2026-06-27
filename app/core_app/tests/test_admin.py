from django.test import TestCase
from django.contrib.auth  import get_user_model
from django.urls import reverse
from django.test import Client



class AdminSiteTests(TestCase):
    def setUp(self):
        """Create user and client for testing superuser access to admin site"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="adminpass"
        )
        # Force login the admin user to access the admin site
        self.client.force_login(self.admin_user)

        # Create a regular user for testing
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password="userpass",
            name="Test User"
        )
    # Test that users are listed on the user page in the admin site
    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse("admin:accounts_user_changelist") #according to user model in accounts app
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_edit_user_page(self):
        """Test that the edit user page works"""
        url = reverse("admin:accounts_user_change", args=[self.user.id]) # according to user model in accounts app
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)    
