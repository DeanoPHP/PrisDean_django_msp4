from datetime import date, time
from django.contrib.auth.models import User
from django.test import TestCase
from .forms import BookingForm

from .models import Booking, AvailableTimeSlots


"""
Tests for the bookings application.

These tests check that the Booking and AvailableTimeSlots models
behave as expected. They test the default booking status, the
Booking string representation, and the creation of available
booking time slots.
"""
class BookingModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123",
            email="test@example.com",
        )

    def test_booking_created_with_pending_status(self):
        booking = Booking.objects.create(
            user=self.user,
            booking_date=date(2026, 8, 20),
            booking_time=time(10, 0),
        )

        self.assertEqual(booking.status, "pending")

    def test_booking_str_method(self):
        booking = Booking.objects.create(
            user=self.user,
            booking_date=date(2026, 8, 20),
            booking_time=time(10, 0),
        )

        expected = "testuser - 2026-08-20"

        self.assertEqual(str(booking), expected)

    def test_available_time_slot_can_be_created(self):
        slot = AvailableTimeSlots.objects.create(
            date=date(2026, 8, 20),
            time=time(10, 0),
            is_active=True,
        )

        self.assertTrue(slot.is_active)
        self.assertEqual(slot.date, date(2026, 8, 20))
        self.assertEqual(slot.time, time(10, 0))


"""
Booking form tests.

These tests check that the booking form correctly validates
appointment dates and times. They confirm that an available
time slot can be booked, an unavailable time slot is rejected,
and an already booked time slot cannot be booked again.
"""
class BookingFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="formuser",
            password="testpass123",
            email="form@example.com",
        )

        self.slot = AvailableTimeSlots.objects.create(
            date=date(2026, 8, 25),
            time=time(11, 0),
            is_active=True,
        )

    # Test that a valid available slot passes form validation.
    def test_valid_booking_form(self):
        form = BookingForm(
            data={
                "booking_date": date(2026, 8, 25),
                "booking_time": time(11, 0),
            }
        )

        self.assertTrue(form.is_valid())

    # Test that an unavailable slot is rejected.
    def test_unavailable_slot_is_rejected(self):
        form = BookingForm(
            data={
                "booking_date": date(2026, 8, 26),
                "booking_time": time(12, 0),
            }
        )

        self.assertFalse(form.is_valid())

    # Test that an already booked slot is rejected.
    def test_duplicate_booking_is_rejected(self):
        Booking.objects.create(
            user=self.user,
            booking_date=date(2026, 8, 25),
            booking_time=time(11, 0),
            status="confirmed",
        )

        form = BookingForm(
            data={
                "booking_date": date(2026, 8, 25),
                "booking_time": time(11, 0),
            }
        )

        self.assertFalse(form.is_valid())