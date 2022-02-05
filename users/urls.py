from django.urls import path

from users.views import SignUpFormView, SignInFormView, sign_out, AccountTemplateView

app_name = 'users'

urlpatterns = [
    path('', SignUpFormView.as_view(), name='home'),
    path('sign-in/', SignInFormView.as_view(), name='sign-in'),
    path('sign-out/', sign_out, name='sign-out'),
    path('account/', AccountTemplateView.as_view(), name='account'),
]


