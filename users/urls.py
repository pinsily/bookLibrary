from django.conf.urls import url

from users import views

app_name = "users"

urlpatterns = [
    url("login/", views.user_login, name="login"),
    url("logout", views.user_logout, name="logout"),
    url("register/", views.user_register, name="register"),
]
