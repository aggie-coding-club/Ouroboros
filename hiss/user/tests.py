from django.test import TestCase

from user.models import User


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        self.email = "dummy@email.com"
        self.password = "password"

    def test_email_is_lookup(self):
        created_user = User.objects.create_user(self.email, self.password)

        self.assertTrue(User.objects.filter(email=self.email).exists())