from django.urls import path
from .views import home, about_us, login_view, register, contact, logout_view

app_name= "core"

urlpatterns = [
    path("", home, name="home"),
    path("sobre_nosotros/", about_us, name="about_us"),   
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("registro/", register, name="register"),
    path("contacta_con_nosotros/", contact, name="contact"), 
]