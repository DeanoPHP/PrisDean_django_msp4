from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import BookingForm
from .models import Booking


@login_required
def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.save()

            messages.success(request, "Your booking has been created.")
            return redirect("home")

    else:
        form = BookingForm()

    return render(
        request,
        "bookings/create_booking.html",
        {"form": form},
    )


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(
        user=request.user
    ).order_by("booking_date", "booking_time")

    context = {
        "bookings": bookings,
    }

    return render(
        request,
        "bookings/my_bookings.html",
        context,
    )

