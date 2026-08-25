from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = [
            "name",
            "email",
            "telephone",
            "subject",
            "message",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your email address",
                }
            ),
            "telephone": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Your telephone number",
                }
            ),
            "subject": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "What is your enquiry about?",
                }
            ),
            "message": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "placeholder": "How can we help?",
                    "rows": 5,
                }
            ),
        }