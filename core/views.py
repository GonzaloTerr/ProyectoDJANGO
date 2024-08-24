from django.shortcuts import render
from courses.models import Course
from blog.models import Post
from .form import ContactForm, LoginForm
from .models import Contact
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.urls import reverse

#from django.core.mail import send_mail, Esto es para enviar emails

# Create your views here.
def home(request):
    context={
        "courses":Course.objects.filter(show_home=True),
        "posts":Post.objects.filter(show_home=True),
    }
    return render(request,"core/home.html",context)
    
def about_us(request):
    return render(request,"core/about_us.html")

def login_view(request):
    if request.POST:
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
            else:
                context={"form":form, "error":True, "error_message":"Usuario no valido"}
                return render(request,"core/login.html",context)
        else:
            context={"form":form, "error":True}
            return render(request,"core/login.html",context)
    else:
        form=LoginForm()
        context={"form":form}
        return render(request,"core/login.html",context)

def logout_view(request):
    logout(request)
    return redirect(reverse("core:home"))

def register(request):
    return render(request,"core/register.html")


#def contact(request):
#    if request.POST:
#        nombre=request.POST["nombre"]
#        email=request.POST["email"]
#        comentario=request.POST["comentario"]
#        print(f"Se ha enviado un correo a {nombre} procedente del email {email} con el texto {comentario}")
#    return render(request,"core/contact.html")
def contact(request):
    if request.POST:
        formulario=ContactForm(request.POST)
        if formulario.is_valid():
            nombre=formulario.cleaned_data["nombre"]
            email=formulario.cleaned_data["email"]
            comentario=formulario.cleaned_data["comentario"]
            print(f"Se ha enviado un correo a {nombre} procedente del email {email} con el texto {comentario}")
            
            #message_content=f"nombre {nombre} con email {email} ha escrito: {comenterio}"
            Contact.objects.create(nombre= nombre, email = email, comentario = comentario)

            #success=send_mail(
            #    "Formulario de contacto",
            #    message_content,
            #    "miemailenhosting@mipagima.com",     ESTO ES PARA ENVIAR EMAILS
            #    ["gonzaloterrones@yahoo.com.ar"],
            #    fail_silently=False,
            #)
            
            context={
                "formulario" : formulario,
                "success" : True    #cambio True por success para enviar emails
            }
            return render(request,"core/contact.html",context)
        else:
            context={
                "formulario" : formulario,
            }
            return render(request,"core/contact.html",context)
    formulario=ContactForm()
    context={
        "formulario" : formulario
    }
    return render(request,"core/contact.html",context)