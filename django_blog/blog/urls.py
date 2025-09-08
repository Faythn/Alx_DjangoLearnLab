from django.urls import path
from . import views_auth

urlpatterns = [
    path("login/", views_auth.login_view, name="login"),
    path("logout/", views_auth.logout_view, name="logout"),
    path("register/", views_auth.register_view, name="register"),
    path("profile/", views_auth.profile_view, name="profile"),
]
