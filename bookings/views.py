import stripe
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.utils import timezone

from .forms import BookingForm
from .models import AvailableTimeSlots, Booking


@login_required
def create_booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)

        if form.is_valid():
            booking_date = form.cleaned_data["booking_date"]
            booking_time = form.cleaned_data["booking_time"]

            with transaction.atomic():
                slot = (
                    AvailableTimeSlots.objects.select_for_update()
                    .filter(
                        date=booking_date,
                        time=booking_time,
                        is_active=True,
                    )
                    .first()
                )

                if not slot:
                    form.add_error(
                        None,
                        "This appointment is no longer available. "
                        "Please choose another slot.",
                    )
                else:
                    already_booked = (
                        Booking.objects.filter(
                            booking_date=booking_date,
                            booking_time=booking_time,
                        )
                        .exclude(status="cancelled")
                        .exists()
                    )

                    if already_booked:
                        form.add_error(
                            None,
                            "This appointment has just been booked. "
                            "Please choose another slot.",
                        )
                    else:
                        booking = form.save(commit=False)
                        booking.user = request.user
                        booking.save()

                        return redirect(
                            "create_checkout_session",
                            booking_id=booking.id,
                        )
    else:
        form = BookingForm()

    return render(
        request,
        "bookings/create_booking.html",
        {"form": form},
    )


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by(
        "booking_date", "booking_time"
    )

    context = {
        "bookings": bookings,
    }

    return render(
        request,
        "bookings/my_bookings.html",
        context,
    )


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
        booking.status = "cancelled"
        booking.save()

        messages.success(request, "Your booking has been cancelled.")

        return redirect("my_bookings")

    context = {
        "booking": booking,
    }

    return render(
        request,
        "bookings/delete_booking.html",
        context,
    )


@login_required
def available_slots(request):
    today = timezone.localdate()
    slots = AvailableTimeSlots.objects.filter(
        is_active=True,
        date__gte=today,
    ).order_by("date", "time")

    calendar_events = []

    for slot in slots:
        is_booked = (
            Booking.objects.filter(
                booking_date=slot.date,
                booking_time=slot.time,
            )
            .exclude(status="cancelled")
            .exists()
        )

        if not is_booked:
            calendar_events.append(
                {
                    "id": slot.id,
                    "title": f"Available - {slot.time.strftime('%H:%M')}",
                    "start": (
                        f"{slot.date.isoformat()}" f"T{slot.time.strftime('%H:%M:%S')}"
                    ),
                }
            )

    return JsonResponse(calendar_events, safe=False)


@login_required
def create_checkout_session(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        user=request.user,
    )

    stripe.api_key = settings.STRIPE_SECRET_KEY

    checkout_session = stripe.checkout.Session.create(
        mode="payment",
        line_items=[
            {
                "price_data": {
                    "currency": "gbp",
                    "unit_amount": 10000,
                    "product_data": {
                        "name": "Professional Oven Clean",
                    },
                },
                "quantity": 1,
            }
        ],
        metadata={
            "booking_id": str(booking.id),
            "user_id": str(request.user.id),
        },
        success_url=request.build_absolute_uri(
            "/bookings/payment-success/"
        ) + "?session_id={CHECKOUT_SESSION_ID}",
        cancel_url=request.build_absolute_uri(
            f"/bookings/payment-cancelled/?booking_id={booking.id}"
        ),
    )

    return redirect(checkout_session.url)


@login_required
def payment_success(request):
    return render(
        request,
        "bookings/payment_success.html",
    )


@login_required
def payment_cancelled(request):
    booking_id = request.GET.get("booking_id")

    if booking_id:
        booking = get_object_or_404(
            Booking,
            id=booking_id,
            user=request.user,
        )

        if booking.status == "pending":
            booking.status = "cancelled"
            booking.save()

    return render(
        request,
        "bookings/payment_cancelled.html",
    )


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get("HTTP_STRIPE_SIGNATURE")

    stripe.api_key = settings.STRIPE_SECRET_KEY

    try:
        event = stripe.Webhook.construct_event(
            payload,
            sig_header,
            settings.STRIPE_WEBHOOK_SECRET,
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event["type"] == "checkout.session.completed":
        session = event["data"]["object"]

        booking_id = session["metadata"]["booking_id"]

        if booking_id and session["payment_status"] == "paid":
            try:
                booking = Booking.objects.get(id=booking_id)

                if booking.status == "pending":
                    booking.status = "confirmed"
                    booking.save()

                    send_mail(
                        subject="PrisDean Booking Confirmation",
                        message=(
                            f"Hi {booking.user.first_name or booking.user.username},\n\n"
                            "Thank you for your payment.\n\n"
                            "Your oven cleaning appointment has been confirmed.\n\n"
                            f"Date: {booking.booking_date.strftime('%d %B %Y')}\n"
                            f"Time: {booking.booking_time.strftime('%H:%M')}\n"
                            "Price paid: £100.00\n\n"
                            "Thank you for choosing PrisDean.\n"
                        ),
                        from_email=None,
                        recipient_list=[booking.user.email],
                        fail_silently=False,
                    )

            except Booking.DoesNotExist:
                pass

    return HttpResponse(status=200)