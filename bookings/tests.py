from django.urls import reverse
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


"""
Booking view tests.

These tests check that booking pages are protected correctly
and that users can only access or modify their own bookings.
They also test that cancelling a booking changes its status
to cancelled.
"""


class BookingViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="viewuser",
            password="testpass123",
            email="view@example.com",
        )

        self.other_user = User.objects.create_user(
            username="otheruser",
            password="testpass123",
            email="other@example.com",
        )

        self.booking = Booking.objects.create(
            user=self.user,
            booking_date=date(2026, 8, 28),
            booking_time=time(10, 0),
            status="confirmed",
        )

    # Test that a logged-out user cannot access My Bookings.
    def test_my_bookings_requires_login(self):
        response = self.client.get(reverse("my_bookings"))

        self.assertEqual(response.status_code, 302)

    # Test that a logged-in user can access My Bookings.
    def test_logged_in_user_can_access_my_bookings(self):
        self.client.login(
            username="viewuser",
            password="testpass123",
        )

        response = self.client.get(reverse("my_bookings"))

        self.assertEqual(response.status_code, 200)

    # Test that a user cannot edit another user's booking.
    def test_user_cannot_edit_another_users_booking(self):
        self.client.login(
            username="otheruser",
            password="testpass123",
        )

        response = self.client.get(
            reverse(
                "edit_booking",
                args=[self.booking.id],
            )
        )

        self.assertEqual(response.status_code, 404)

    # Test that a user cannot cancel another user's booking.
    def test_user_cannot_cancel_another_users_booking(self):
        self.client.login(
            username="otheruser",
            password="testpass123",
        )

        response = self.client.post(
            reverse(
                "delete_booking",
                args=[self.booking.id],
            )
        )

        self.assertEqual(response.status_code, 404)

    # Test that a user can cancel their own booking.
    def test_user_can_cancel_own_booking(self):
        self.client.login(
            username="viewuser",
            password="testpass123",
        )

        response = self.client.post(
            reverse(
                "delete_booking",
                args=[self.booking.id],
            )
        )

        self.booking.refresh_from_db()

        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            self.booking.status,
            "cancelled",
        )
