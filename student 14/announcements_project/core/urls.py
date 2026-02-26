from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path("register/", register, name="register"),
    # this adds the login view as a form
    path("login/", auth_views.LoginView.as_view(
        template_name="core/login.html"), name="login",
        ),
    # this adds the logout view
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]