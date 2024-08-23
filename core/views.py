from django.shortcuts import render
from courses.models import Course
from blog.models import Post
from .form import ContactForm
from .models import Contact
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

def login(request):
    return render(request,"core/login.html")

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