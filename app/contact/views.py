from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm
# Create your views here.

def contact(request):
    #print("tipo de peticion: {}".format(request.method))
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name= request.POST.get('name','')
            email= request.POST.get('email','')
            content= request.POST.get('content','')
            #todo ha ido bien y enviamos el correo
            email = EmailMessage(
                'La cafetera: Nuevo mensaje de contacto',
                'De {} <{}>\n\n Escribió:\n\n {}' .format(name,email, content),
                "no-contentestar@inbox.mailtrap.io",
                ["alejandrocursos98@gmail.com"],
                reply_to=[email]
            )
            try:
                #todo ha ido bien
                email.send()
                return redirect(reverse('contact')+"?ok")
            except:
                #algo no fue bion
                return redirect(reverse('contact')+"?nope")

    return render(request,"contact/contact.html", {'form':contact_form})