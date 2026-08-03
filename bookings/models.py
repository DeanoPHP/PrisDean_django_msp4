from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")

    booking_date = models.DateField()
    booking_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
    )

    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.booking_date}"


class AvailableTimeSlots(models.Model):
    date = models.DateField()
    time = models.TimeField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["date", "time"]
        constraints = [
            models.UniqueConstraint(
                fields=["date", "time"],
                name="unique_available_time_slot",
            )
        ]

    def __str__(self):
        return f"{self.date} at {self.time.strftime('%H:%M')}"
