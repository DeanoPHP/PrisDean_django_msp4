from django.urls import path
from . import views

urlpatterns = [
    path("create/", views.create_booking, name="create_booking"),
    path("my_bookings/", views.my_bookings, name="my_bookings"),
    path("edit/<int:booking_id>/", views.edit_booking, name="edit_booking"),
    path("delete/<int:booking_id>/", views.delete_booking, name="delete_booking"),
    path("available-slots/", views.available_slots, name="available_slots"),
    path("create-checkout-session/<int:booking_id>/", views.create_checkout_session, name="create_checkout_session"),
    path("payment-success/", views.payment_success, name="payment_success"),
    path("payment-cancelled/", views.payment_cancelled, name="payment_cancelled"),
]
