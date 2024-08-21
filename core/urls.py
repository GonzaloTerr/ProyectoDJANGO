from django.urls import path
from .views import home, about_us, login, register, contact

app_name= "core"

urlpatterns = [
    path("", home, name="home"),
    path("sobre_nosotros/", about_us, name="about_us"),   
    path("login/", login, name="login"),
    path("registro/", register, name="register"),
    path("contacta_con_nosotros/", contact, name="contact"), 
]