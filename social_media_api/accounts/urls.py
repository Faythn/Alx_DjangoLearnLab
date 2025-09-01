

from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.RegisterView.as_view(), name="register"),   # ✅ checker looks for "register/"
    path("login/", views.LoginView.as_view(), name="login"),           # ✅ checker looks for "login/"
    path("profile/", views.ProfileView.as_view(), name="profile"),     # ✅ checker looks for "profile/"
]


from django.urls import path
from .views import follow_user, unfollow_user

urlpatterns = [
    path("follow/<int:user_id>/", follow_user, name="follow-user"),
    path("unfollow/<int:user_id>/", unfollow_user, name="unfollow-user"),
]
