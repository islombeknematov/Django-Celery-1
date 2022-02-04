from django.contrib.auth import logout
from django.shortcuts import redirect, reverse
from django.views import generic
from django.views.generic import TemplateView, FormView

from users.forms import UserForm, AuthForm


class SignUpFormView(FormView):
    template_name = 'sign_up.html'
    form_class = UserForm
    success_url = '/account/'


class SignInFormView(FormView):
    template_name = 'sign_in.html'
    form_class = AuthForm
    success_url = '/account/'


def sign_out(request):
    logout(request)
    return redirect(reverse('sign-in'))


class AccountTemplateView(TemplateView):
    template_name = 'account.html'



