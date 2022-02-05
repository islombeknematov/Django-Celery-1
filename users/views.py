from django.contrib.auth import logout
from django.shortcuts import redirect, reverse
from django.views import generic
from django.views.generic import TemplateView, FormView

from users.forms import UserForm, AuthForm

from django.contrib.auth import logout, login, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class SignUpFormView(FormView):
    template_name = 'sign_up.html'
    form_class = UserForm
    success_url = '/account/'

    def form_valid(self, form):
        obj = form.save()
        login(self.request, obj)
        return super().form_valid(form)


class SignInFormView(FormView):
    template_name = 'sign_in.html'
    form_class = AuthForm
    success_url = '/account/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(SignInFormView, self).form_valid(form)
        else:
            return self.form_valid(form)


def sign_out(request):
    logout(request)
    return redirect(reverse('sign-in'))


class AccountTemplateView(TemplateView):
    template_name = 'account.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
