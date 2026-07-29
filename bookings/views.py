from django.shortcuts import render, redirect, get_object_or_404
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


@login_required
@login_required

def edit_booking(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user,
    )

    if request.method == "POST":
        form = BookingForm(request.POST, instance=booking)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Booking updated successfully.",
            )

            return redirect("my_bookings")

    else:
        form = BookingForm(instance=booking)

    context = {
        "form": form,
        "booking": booking,
    }

    return render(
        request,
        "bookings/edit_booking.html",
        context,
    )
    

@login_required
def delete_booking(request, booking_id):
    booking = get_object_or_404(
        Booking, 
        id=booking_id,
        user=request.user,
    )

    if request.method == "POST":
        booking.delete()

        messages.success(
            request,
            "Your booking has been cancelled successfully."
        )

        return redirect("my_bookings")

    context = {
        "booking": booking,
    }

    return render(
        request,
        "bookings/delete_booking.html",
        context,
    )