from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView, FormView

from users.forms import UserForm, AuthForm

from django.contrib.auth import logout, login, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from users.decorators import login_forbidden

from users.tasks import create_email


class SignUpFormView(FormView):
    template_name = 'sign_up.html'
    form_class = UserForm
    success_url = '/account/'

    def form_valid(self, form):
        obj = form.save()
        login(self.request, obj)

        # This is a Celery task
        create_email.delay(
            user_id=obj.id,  # user ID - this must be added
            email_account="Do not reply",  # the email account being used
            subject=obj.username,  # who to mail
            cc=[],
            template="hello.html",  # template to be used
        )
        # End Celery task
        return super().form_valid(form)

    @method_decorator(login_forbidden)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


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

    @method_decorator(login_forbidden)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


def sign_out(request):
    logout(request)
    return redirect(reverse('users:sign-in'))


class AccountTemplateView(TemplateView):
    template_name = 'account.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

