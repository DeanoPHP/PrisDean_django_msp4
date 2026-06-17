# PrisDean Cleaning Services

## Overview

PrisDean is a Django-based cleaning service booking platform built as Code Institute Milestone Project 4.

The website allows customers to:

- Register and log in securely
- Create and manage a user profile
- Book cleaning appointments through an interactive calendar
- Pay securely online using Stripe
- View and manage their bookings

The project is built using modern web development technologies and follows best practices for full-stack development.

---

## Technologies Used

### Backend

- Python
- Django
- PostgreSQL
- Django Allauth
- Stripe

### Frontend

- HTML5
- CSS3
- Bootstrap 5
- JavaScript

### Development & Deployment

- Docker
- Git
- GitHub

---

## Features

### User Accounts

- User registration
- User login/logout
- Automatic profile creation using Django signals

### Booking System

- Calendar-based booking system
- Appointment management
- Availability control

### Payments

- Secure Stripe payment integration

### Admin Features

- Manage bookings
- Manage users
- Manage available appointment slots

---

## Database Structure

### User

- Django built-in User model
- Authentication handled by Django Allauth

### Profile

- One-to-One relationship with User
- Stores customer information

### Booking

- Customer booking details
- Date and time slot
- Booking status
- Payment status

---

## Future Features

- Email booking confirmations
- SMS notifications
- Customer reviews
- Admin dashboard analytics
- Recurring bookings
- Service history

---

## Running the Project Locally

### Clone the Repository

```bash
git clone https://github.com/yourusername/prisdean.git
cd prisdean
```

### Create Environment Variables

Create a `.env` file in the project root and add the required environment variables.

### Build the Docker Containers

```bash
docker compose build
```

### Start the Application

```bash
docker compose up
```

### Apply Migrations

Open a new terminal and run:

```bash
docker compose exec web python manage.py migrate
```

### Create a Superuser

```bash
docker compose exec web python manage.py createsuperuser
```

### Access the Website

Open your browser and navigate to:

```
http://127.0.0.1:8000
```

### Access Django Admin

```
http://127.0.0.1:8000/admin
```

---

## Testing

Testing documentation will be added during development and prior to project submission.

---

## Deployment

Deployment instructions will be added once the project is ready for production.

---

## Author

**Dean Lark**

Created as part of the Code Institute Full Stack Development Diploma.