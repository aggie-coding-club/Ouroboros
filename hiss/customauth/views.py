from django import views
from django.conf import settings
from django.contrib.auth import get_user_model, login
from django.contrib.auth import views as auth_views
from django.contrib.sites import shortcuts as site_shortcuts
from django.contrib.sites.requests import RequestSite
from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.views import generic

from customauth import forms as customauth_forms
from customauth.tokens import email_confirmation_generator
from user.models import User


def send_confirmation_email(curr_domain: RequestSite, user: User) -> None:
    subject = "Confirm your email address!"
    template_name = "registration/emails/activate_email.html"
    context = {
        "user": user,
        "domain": curr_domain,
        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
        "token": email_confirmation_generator.make_token(user),
        "event_name": settings.EVENT_NAME,
    }
    user.send_html_email(template_name, context, subject)


# Create your views here.
class SignupView(generic.FormView):
    form_class = customauth_forms.SignupForm
    template_name = "registration/signup.html"

    def form_valid(self, form):
        user: User = form.save(commit=False)
        user.is_active = False
        user.save()
        curr_domain = site_shortcuts.get_current_site(self.request)
        send_confirmation_email(curr_domain, user)
        return render(self.request, "registration/check_email.html")


class ResendActivationEmailView(generic.FormView):
    form_class = customauth_forms.ResendActivationEmailForm
    template_name = "registration/resend_email.html"

    def form_valid(self, form):
        user: User = get_object_or_404(User, email=form.cleaned_data["email"])
        curr_domain = site_shortcuts.get_current_site(self.request)
        send_confirmation_email(curr_domain, user)
        return render(self.request, "registration/check_email.html")


class ActivateView(views.View):
    def get(self, request, *args, **kwargs):
        hacker = None
        try:
            uid = force_text(urlsafe_base64_decode(kwargs["uidb64"]))
            hacker = get_user_model().objects.get(id=int(uid))
        except (
                TypeError,
                ValueError,
                OverflowError,
                get_user_model().DoesNotExist,
        ) as e:
            print(e)
        if hacker is not None and email_confirmation_generator.check_token(
                hacker, kwargs["token"]
        ):
            hacker.is_active = True
            hacker.save()
            login(request, hacker)
            return redirect(reverse_lazy("status"))
        else:
            return HttpResponse("Activation link is invalid.")


class PlaceholderPasswordResetView(auth_views.PasswordResetView):
    """
    Uses PlaceholderPasswordResetForm instead of default PasswordResetForm.
    """

    form_class = customauth_forms.PlaceholderPasswordResetForm


class PlaceholderPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    """
    Uses PlaceholderSetPasswordForm instead of default SetPasswordForm.
    """

    form_class = customauth_forms.PlaceholderSetPasswordForm
