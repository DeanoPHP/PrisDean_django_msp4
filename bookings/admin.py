from django.contrib import admin

from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "booking_date",
        "booking_time",
    )

    list_filter = (
        "booking_date",
    )

    search_fields = (
        "user__username",
        "user__email",
    )

    ordering = (
        "booking_date",
        "booking_time",
    )