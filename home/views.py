from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import ContactForm


def home(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Thank you for your message. We will get back to you soon."
            )
            return redirect("contact")

    else:
        form = ContactForm()

    context = {
        "form": form,
    }

    return render(request, "home/contact.html", context)

def services(request):
    return render(request, "home/services.html")