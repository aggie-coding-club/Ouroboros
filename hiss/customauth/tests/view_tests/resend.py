import re

from django.core import mail
from django.urls import reverse_lazy

from shared import test_case
from user.models import User

from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from customauth.tokens import email_confirmation_generator


URL_REGEX = r"(?P<url>https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*))"


class ResendActivationEmailView(test_case.SharedTestCase):
    def isValidLink(self, user, url):
        valid_uid =  urlsafe_base64_encode(force_bytes(user.pk))
        valid_token =  email_confirmation_generator.make_token(user)

        url_split = url.split('/')

        return url_split[-2] == valid_token and url_split[-3] == valid_uid

    def setUp(self):
        self.email = "hacker@tamu.edu"
        self.password = "dummypassword"
        self.inactive_user = User.objects._create_user(
            email=self.email, password=self.password
        )


    def test_submitting_valid_form_sends_email(self):
        fields = {"email": self.email}
        User.objects.get(**fields)
        self.client.post(reverse_lazy("customauth:resend_email"), fields)
        self.assertEqual(len(mail.outbox), 1)
        body, _ = mail.outbox[0].alternatives[0]
        url, _, _ = re.findall(URL_REGEX, body)[0]
        user = User.objects.get(email=self.email)

        self.assertTrue(self.isValidLink(user, url))


    def test_clicking_sent_email_link_is_valid(self):
        fields = {"email": self.email}
        User.objects.get(**fields)
        self.client.post(reverse_lazy("customauth:resend_email"), fields)
        self.assertEqual(len(mail.outbox), 1)
        body, _ = mail.outbox[0].alternatives[0]
        url, _, _ = re.findall(URL_REGEX, body)[0]
        user = User.objects.get(email=self.email)

        self.assertTrue(self.isValidLink(user, url))