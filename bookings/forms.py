from django import forms
from .models import AvailableTimeSlots, Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ["booking_date", "booking_time"]

        widgets = {
            "booking_date": forms.DateInput(
                attrs={
                    "type": "date",
                    "class": "form-control",
                    "readonly": True,
                }
            ),
            "booking_time": forms.TimeInput(
                attrs={
                    "type": "time",
                    "class": "form-control",
                    "readonly": True,
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

        if not booking_date or not booking_time:
            return cleaned_data

        slot_exists = AvailableTimeSlots.objects.filter(
            date=booking_date,
            time=booking_time,
            is_active=True,
        ).exists()

        if not slot_exists:
            raise forms.ValidationError(
                "This appointment is not available. "
                "Please choose a slot from the calendar."
            )

        existing_bookings = Booking.objects.filter(
            booking_date=booking_date,
            booking_time=booking_time,
        ).exclude(status="cancelled")

        # When editing, exclude the current booking from the check.
        if self.instance and self.instance.pk:
            existing_bookings = existing_bookings.exclude(pk=self.instance.pk)

        if existing_bookings.exists():
            raise forms.ValidationError(
                "This appointment has already been booked. "
                "Please choose another available slot."
            )

        return cleaned_data
