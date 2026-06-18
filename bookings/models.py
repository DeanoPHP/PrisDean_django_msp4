from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="bookings"
    )

    booking_date = models.DateField()
    booking_time = models.TimeField()

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.booking_date}"
