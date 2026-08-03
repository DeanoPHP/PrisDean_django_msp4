from django.contrib import admin

from .models import Booking, AvailableTimeSlots


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "booking_date",
        "booking_time",
        "status",
    )

    list_filter = (
        "status",
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


@admin.register(AvailableTimeSlots)
class AvailableTimeSlotAdmin(admin.ModelAdmin):
    list_display = (
        "date", 
        "time", 
        "is_active"
    )

    list_filter = (
        "is_active", 
        "date"
    )

    ordering = (
        "date", 
        "time"
    )