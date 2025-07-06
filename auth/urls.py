from django.urls import path

from .register import RegisterView
from .profile import ProfilePageView
from .logout import LogoutView
from .login import LoginView
from .change_password import ChangePasswordView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfilePageView.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
]
