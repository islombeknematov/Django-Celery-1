from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from users.views import SignUpFormView, SignInFormView, sign_out, AccountTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', SignUpFormView.as_view(), name='home'),
    path('sign-in/', SignInFormView.as_view(), name='sign-in'),
    path('sign-out/', sign_out, name='sign-out'),
    path('account/', AccountTemplateView.as_view(), name='sign-out'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
