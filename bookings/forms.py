from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["booking_date", "booking_time"]

        widgets = {
            "booking_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                }
            ),
            "booking_time": forms.TimeInput(
                attrs={
                    "type": "time",
                    "class": "form-control",
                }
            ),
        }

        labels = {
            "booking_date": "Choose a date",
            "booking_time": "Choose a time",
        }
