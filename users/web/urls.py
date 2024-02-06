from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import user_login, user_logout, user_signup, user_detail

urlpatterns = [
    path("login/", user_login, name="login"),
    path("signup/", user_signup, name="signup"),
    path("logout/", user_logout, name="logout"),
    path("profile/", login_required(user_detail, login_url="login"), name="user_detail"),
]