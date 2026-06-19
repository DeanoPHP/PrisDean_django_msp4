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

    def clean(self):
        cleaned_data = super().clean()

        booking_date = cleaned_data.get("booking_date")
        booking_time = cleaned_data.get("booking_time")

        if booking_date and booking_time:
            booking_exists = Booking.objects.filter(
                booking_date=booking_date,
                booking_time=booking_time,
            ).exists()

            if booking_exists:
                raise forms.ValidationError(
                    "This date and time already exists. Please choose a different date and time."
                )
