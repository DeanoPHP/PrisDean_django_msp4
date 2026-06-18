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

## User Profile Automation

To improve the user experience, a profile is automatically created whenever a new user registers.

### Technologies Used

- Django Signals
- Django Allauth
- One-to-One Relationships

### How It Works

When a user successfully registers through Django Allauth, a Django signal listens for the creation of a new User object.

The signal automatically creates a corresponding Profile object linked to the user through a One-to-One relationship.

This ensures that every registered user has a profile without requiring additional setup steps.

### Example Signal

```python
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
```

---

## Project Architecture

### Authentication

- Django Allauth handles user registration and login.
- Authentication templates are customised to match the site design.

### Profile Management

- A Profile model extends Django's built-in User model.
- Profiles are automatically created using Django Signals.

### Database

- PostgreSQL is used as the primary database.
- Relationships are managed using Django ORM.

### Containerisation

- Docker is used to ensure a consistent development environment.
- PostgreSQL and Django run in separate containers managed by Docker Compose.
```

### Benefits

- Profiles are created automatically
- Prevents missing profile records
- Simplifies user onboarding
- Demonstrates Django signal implementation
```
---

## Wireframes




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

## Why Docker?

Although Docker was not a requirement for this project, it was chosen to provide a consistent and reproducible development environment.

### Benefits

- Ensures the project runs the same way on any machine.
- Simplifies project setup for assessors and developers.
- Isolates project dependencies from the host operating system.
- Allows Django and PostgreSQL to run in separate containers.
- Reflects modern industry development practices.

### What Docker Manages

The project uses Docker Compose to manage:

- Django application container
- PostgreSQL database container

This allows the application to be started with a single command:

```bash
docker compose up
```

### Learning Outcomes

Implementing Docker helped develop an understanding of:

- Containerisation
- Multi-container applications
- Environment management
- Database services
- Deployment preparation

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