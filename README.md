![PrisDean responsive design](static/images/responsive.png)

[Click here to go to PrisDean.com](https://www.prisdean.com)

# PrisDean
PrisDean is a full-stack Django web application for an oven cleaning
business. The application allows customers to create an account, view
available appointment slots, book an oven cleaning service and securely
pay for their booking using Stripe.

The website provides customers with a simple booking process while also
providing the business administrator with tools to manage available
appointment slots and customer bookings.

## Project Goals

The main goal of PrisDean is to provide an easy-to-use online booking
system for customers who want to arrange a professional oven cleaning
service.

The application was designed to allow customers to:

- Create and manage a user account.
- View available oven cleaning appointments.
- Select a booking date and time using an interactive calendar.
- Prevent unavailable or already booked appointments from being selected.
- Pay securely for their booking using Stripe.
- View their existing bookings.
- Reschedule or cancel a booking.
- Receive email confirmation when a booking is confirmed.
- Receive email confirmation when a booking is cancelled.

The application also provides administration functionality that allows
the business owner to manage available appointment slots and customer
bookings through the Django administration panel.

---

## User Stories

User stories were used during the development of PrisDean to identify
the main requirements of the application from both the customer and
business administrator perspectives.

### Customer User Stories

As a customer, I want to:

- Register for an account so that I can make and manage bookings.
- Log in and log out securely.
- View available appointment dates and times on a calendar.
- Select an available appointment slot for my oven cleaning.
- Be prevented from selecting a time slot that has already been booked.
- View my existing bookings.
- Reschedule an existing booking if I need to change my appointment.
- Cancel a booking that I no longer require.
- Pay securely for my oven cleaning using Stripe.
- See confirmation that my payment was successful.
- Receive an email confirming my booking after successful payment.
- Receive an email when I cancel a confirmed booking.
- View the current status of my booking.

### Administrator User Stories

As the business administrator, I want to:

- Access the Django administration panel securely.
- Create available appointment dates and times.
- Activate or deactivate appointment slots.
- View customer bookings.
- View the status of each booking.
- Update booking information when necessary.
- Prevent booked appointment slots from being offered to another customer.

### Site Owner Goals

As the site owner, I want the application to:

- Provide customers with a simple and clear booking process.
- Securely process online payments.
- Automatically confirm bookings following successful payment.
- Make cancelled appointment slots available again.
- Reduce the need to manually manage appointments.
- Provide a central administration area for managing bookings and availability.

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
- Customer reviews
- Recurring bookings
- Multiple cleaning services
- Payment reciepts
- Rescheduling confirmtion
- Follow up emails after cleaning
- Additional payment options

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

## UX and Design

The design of PrisDean focuses on providing customers with a simple,
clear and easy-to-use booking experience.

The booking process was designed to minimise the number of steps
required for a customer to choose an appointment and complete payment.

### Design Approach

The interface uses a clean and modern design suitable for a
professional oven cleaning business.

Bootstrap is used throughout the project to provide consistent
components and responsive layouts, with additional custom CSS used
to give PrisDean its own visual identity.

### Navigation

The navigation bar provides clear access to the main areas of the
website.

Navigation options change depending on the authentication status of
the user.

Logged-out users are provided with options to register or log in,
while authenticated users can access their account and booking
functionality.

### Home Page

The home page introduces the PrisDean oven cleaning service using a
large hero section and clear calls to action.

Additional sections explain how the service works and provide
information to help customers decide whether to make a booking.

### Booking Experience

The booking interface was designed to make appointment selection
simple.

FullCalendar provides customers with a visual representation of
available appointments.

Only appointment slots created by the administrator and currently
available for booking are displayed.

After choosing an appointment, the customer is directed through the
booking and Stripe payment process.

### Feedback to the User

Django messages are used throughout the application to provide
feedback following important actions.

Examples include confirmation that:

- A booking has been created.
- A booking has been updated.
- A booking has been cancelled.

Dedicated pages are also displayed following successful or cancelled
Stripe payments.

### Responsive Design

PrisDean was designed to work across different screen sizes.

Bootstrap's responsive layout system and custom CSS media queries are
used to adjust the layout for desktop, tablet and mobile devices.

Special attention was given to the navigation, hero content, forms
and booking interface to ensure that they remain usable on smaller
screens.

## Wireframes

Figma was used to create the wireframes for the PrisDean website. The wireframes helped plan the layout and structure of each page before development, including the placement of navigation, content sections, buttons and other key elements. Desktop and mobile wireframes were created to help plan a responsive design across different screen sizes.

### Home desktop layout
![Home Page desktop Wireframe](static/images/wireframes/home-desktop.png)

### Home mobile layout
![Home Page mobile Wireframe](static/images/wireframes/home-mobile.png)

### Services desktop layout
![Services Page desktop Wireframe](static/images/wireframes/services-desktop.png)

### services mobile layout
![Services Page mobile Wireframe](static/images/wireframes/services-mobile.png)

### Booking layout
![Booking Page Wireframe](static/images/wireframes/booking.png)

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
## Technologies Used

A range of technologies, frameworks and development tools were used
to build the PrisDean application.

### Languages

- **Python** - Used for the backend application logic.
- **HTML5** - Used to structure the website pages.
- **CSS3** - Used for custom styling and responsive design.
- **JavaScript** - Used for interactive functionality including the
  booking calendar.

### Frameworks and Libraries

- **Django** - Main Python web framework used to build the application.
- **Django Allauth** - Provides user registration, login and logout
  functionality.
- **Bootstrap** - Used to create a responsive layout and reusable
  interface components.
- **Bootstrap Icons** - Used for icons throughout the interface.
- **FullCalendar** - Used to display available appointment dates and
  times through an interactive calendar.
- **Stripe** - Used to securely process customer payments.
- **Pillow** - Used to support image handling for user profile images.
- **psycopg2-binary** - Provides the connection between Django and
  PostgreSQL.

### Brevo

Brevo is used for transactional communication within the application.

It provides:

- SMTP delivery for customer booking confirmation emails.
- Transactional SMS messages for customer booking confirmations.
- SMS notifications to the business owner when a new booking is confirmed.

Sensitive Brevo credentials are stored as Heroku Config Vars and are not
committed to the GitHub repository.

### Email and SMS Booking Notifications

When a customer successfully completes payment through Stripe, the booking
is automatically confirmed using a Stripe webhook.

The customer then receives:

- A booking confirmation email containing the appointment date, time and
  amount paid.
- An SMS confirmation containing the appointment date and time.

The business owner also receives an SMS notification when a new paid booking
is confirmed.

Transactional emails are sent using Brevo SMTP, while SMS notifications are
sent using the Brevo transactional SMS API.

Customer telephone numbers entered in UK format are converted to international
format before being sent to the SMS service.

### Database

- **PostgreSQL** - Used as the relational database for storing users,
  profiles, bookings and available appointment slots.

### Development Tools

- **Docker** - Used to provide a consistent development environment
  for the Django application and PostgreSQL database.
- **Docker Compose** - Used to manage the application and database
  containers.
- **Git** - Used for version control throughout development.
- **GitHub** - Used to store and manage the project's source code.
- **VS Code** - Used as the main code editor.

### Code Quality and Testing

- **Black** - Used to automatically format Python code and maintain
  consistent code style.
- **Flake8** - Used to check Python code against coding standards and
  identify potential issues.
- **Django TestCase** - Used to create automated tests for models,
  forms and views.

### External Services

- **Stripe Checkout** - Provides the secure hosted payment page.
- **Stripe Webhooks** - Used to notify the application when a payment
  has successfully completed.
- **Stripe CLI** - Used during local development to test webhook
  events.

---

## Wireframes

## Add wireframes here
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

Testing was carried out throughout the development of PrisDean to
ensure that the main features of the application work as expected.

The project uses a combination of automated Django tests, manual
testing and Python code quality tools.

### Automated Testing

Django's built-in testing framework was used to test important parts
of the booking application.

The automated tests are located in:

`bookings/tests.py`

The tests cover the Booking and AvailableTimeSlots models, booking
form validation and access to booking views.

Tests can be run inside the Docker container using:

    docker compose exec web python manage.py test

### Model Testing

Tests were created for the Booking and AvailableTimeSlots models.

The model tests check that:

- A newly created booking has a default status of `pending`.
- The Booking model returns the expected string representation.
- An active available time slot can be successfully created.

### Form Testing

The BookingForm was tested to ensure that appointment selection is
validated correctly.

The form tests check that:

- A valid available appointment slot passes validation.
- A date and time that is not an available slot is rejected.
- An appointment slot that has already been booked cannot be booked
  again.

This helps prevent customers from creating bookings for unavailable
appointments or double-booking an existing appointment.

### View Testing

Tests were also created for the booking views.

The view tests check that:

- A logged-out user cannot access the My Bookings page.
- A logged-in user can access their My Bookings page.
- A user cannot edit another user's booking.
- A user cannot cancel another user's booking.
- A user can cancel their own booking.
- Cancelling a booking correctly changes its status to `cancelled`.

These tests help ensure that booking information is protected and
customers can only manage bookings that belong to their own account.

### Manual Testing

Manual testing was carried out throughout development in addition to
the automated tests.

The following functionality was manually tested:

| Feature | Test | Result |
| --- | --- | --- |
| Registration | Create a new customer account | Pass |
| Login | Log in using valid account details | Pass |
| Logout | Log out of an authenticated account | Pass |
| Profile | View customer profile information | Pass |
| Calendar | Display active available appointment slots | Pass |
| Booking | Select an available date and time | Pass |
| Double booking | Attempt to select an already booked slot | Pass |
| My Bookings | Display bookings belonging to the logged-in user | Pass |
| Rescheduling | Change an existing appointment | Pass |
| Cancellation | Cancel an existing booking | Pass |
| Booking status | Confirm booking status updates correctly | Pass |
| Stripe Checkout | Redirect customer to Stripe payment page | Pass |
| Stripe payment | Complete a payment using Stripe test mode | Pass |
| Stripe webhook | Confirm booking after successful payment | Pass |
| Cancelled payment | Cancel pending booking when Stripe Checkout is cancelled | Pass |
| Confirmation email | Generate email after successful payment | Pass |
| Cancellation email | Generate email after booking cancellation | Pass |

### Stripe Testing

Stripe was tested using Stripe's test environment.

Test payments were made through Stripe Checkout and the Stripe CLI was
used during local development to forward webhook events to the Django
application.

The payment workflow was tested to ensure that:

1. A new booking begins with a `pending` status.
2. The customer is redirected to Stripe Checkout.
3. A successful payment generates a Stripe webhook event.
4. The webhook changes the booking status to `confirmed`.
5. A booking confirmation email is generated.
6. Cancelling the Stripe Checkout process changes the pending booking
   to `cancelled`.

No real card payments were used during development.

### Code Quality

Black and Flake8 were used throughout development to maintain Python
code quality.

Black was run using:

    docker compose exec web black .

Flake8 was run using:

    docker compose exec web flake8 .

Black was used to provide consistent Python formatting, while Flake8
was used to identify issues such as unused imports and code that did
not meet Python style guidelines.

### Test Results

Before completion of the project, the automated test suite was run
using:

    docker compose exec web python manage.py test

All implemented automated tests passed successfully.

---

## Bugs and Fixes

During development, several issues were encountered and resolved.
Some of the main bugs and their solutions are documented below.

### Available Time Slot Model Import

**Problem:**  
The application failed to start because the booking form attempted to
import `AvailableTimeSlot`, while the model was named
`AvailableTimeSlots`.

The error returned was:

    ImportError: cannot import name 'AvailableTimeSlot'

**Solution:**  
The import was updated to use the correct `AvailableTimeSlots` model
name throughout the booking application.

### Stripe API Key Not Available

**Problem:**  
When Stripe Checkout was first implemented, Stripe returned an
authentication error because the API key was not available to the
application.

**Solution:**  
Stripe test keys were added as environment variables and loaded through
the Django settings. The Stripe secret key is then supplied when
creating Checkout sessions.

Sensitive Stripe keys are not stored directly in the source code.

### Am I Responsive - Website Would Not Display

**Bug:**  
When testing the deployed PrisDean website using Am I Responsive, the
Heroku site would not display inside the device previews.

**Cause:**  
Am I Responsive loads websites inside an iframe. Django's built-in
clickjacking protection prevented the PrisDean homepage from being displayed
inside an external iframe.

**Fix:**  
I temporarily imported Django's `xframe_options_exempt` decorator and applied
it to the homepage view:

    from django.views.decorators.clickjacking import xframe_options_exempt


    @xframe_options_exempt
    def home(request):
        return render(request, "home/index.html")

This allowed the homepage to load correctly inside Am I Responsive so that
the responsive design could be tested and documented.

Once the responsive screenshot had been created, the exemption was removed
so that Django's normal clickjacking protection remained enabled on the
deployed application.

### Stripe Webhook Secret

**Problem:**  
The Stripe webhook initially returned a server error because the
webhook signing secret was not available.

The application attempted to verify the Stripe signature using a
`None` value.

**Solution:**  
The Stripe webhook signing secret was added to the environment
configuration and loaded through Django settings.

This allowed Django to verify that webhook requests genuinely
originated from Stripe.

### Stripe Metadata

**Problem:**  
The webhook initially had difficulty retrieving the booking ID from
the Stripe Checkout Session metadata.

This prevented the application from identifying which booking should
be confirmed following payment.

**Solution:**  
The booking ID is now added to the Checkout Session metadata when the
Stripe session is created.

The webhook retrieves this ID and uses it to locate and update the
correct booking.

### Double Booking

**Problem:**  
Customers needed to be prevented from selecting an appointment that
had already been booked by another customer.

**Solution:**  
Booking form validation checks for an existing booking with the same
date and time.

The available-slots endpoint also checks existing bookings before
displaying appointment slots on the calendar.

Cancelled bookings are excluded from this check so that cancelled
appointment slots can become available again.

### Unpaid Bookings Blocking Appointment Slots

**Problem:**  
A booking was created before the customer completed Stripe Checkout.
If the customer cancelled the payment process, the pending booking
could continue to occupy the appointment slot.

**Solution:**  
The Stripe cancellation URL includes the booking ID. When the customer
returns to the payment-cancelled page, the pending booking is changed
to `cancelled`.

This releases the appointment slot so another customer can book it.

### Flake8 Unused Imports

**Problem:**  
Flake8 identified several unused imports in automatically generated
Django files and application files.

**Solution:**  
Unused imports were removed where they were not required. The project
was checked again using Flake8 to ensure the Python code met the
required coding standards.

---

## Deployment

PrisDean is deployed using Heroku with a Heroku PostgreSQL database.

### Live Site

The deployed application can be accessed at:

https://prisdean-684be6a15d1e.herokuapp.com/

### Heroku Deployment

The following steps were used to deploy the project:

1. Create a new application in Heroku.
2. Add Heroku Postgres to the application.
3. Add the required environment variables using Heroku Config Vars.
4. Install Gunicorn, WhiteNoise and dj-database-url.
5. Create a `Procfile` containing:

       web: gunicorn config.wsgi

6. Create a `.python-version` file containing:

       3.12

7. Configure Django to use the Heroku `DATABASE_URL`.
8. Configure WhiteNoise for static files.
9. Add the Heroku application domain to `ALLOWED_HOSTS`.
10. Connect the local Git repository to Heroku.
11. Deploy the application using:

       git push heroku main

12. Apply the database migrations:

       heroku run python manage.py migrate -a prisdean

13. Create the administrator account:

       heroku run python manage.py createsuperuser -a prisdean

### Environment Variables

Sensitive information is stored using Heroku Config Vars and is not
committed to the GitHub repository.

The deployed application requires environment variables including:

- `EMAIL_HOST_USER` - Brevo SMTP username.
- `EMAIL_HOST_PASSWORD` - Brevo SMTP key.
- `DEFAULT_FROM_EMAIL` - verified sender used for customer emails.
- `BREVO_API_KEY` - API key used for transactional SMS messages.
- `OWNER_PHONE` - business owner's telephone number for booking notifications.

### Stripe Webhook

A Stripe webhook is used to securely confirm successful payments.

The application listens for the:

    checkout.session.completed

event.

When a successful payment is received, the application:

1. Retrieves the associated booking.
2. Changes the booking status from `pending` to `confirmed`.
3. Sends the customer a confirmation email using Brevo.
4. Sends the customer a booking confirmation SMS using Brevo.
5. Sends the business owner an SMS notification containing the new booking
   details.

This ensures that bookings are only confirmed after Stripe has successfully
processed the payment.

### Production Configuration

The deployed application runs with Django debug mode disabled.

Static files are served using WhiteNoise and the production application
is served using Gunicorn.

---

## Credits and Acknowledgements

I would like to thank the instructors and teaching staff at Code

Institute for their guidance and support throughout the course and

during the development of this project.

I would also like to thank the staff at Bristol College for their

continued support, encouragement and patience throughout my studies.

Their help has been greatly appreciated.

### Learning Resources

During the development of PrisDean, I used a number of learning

resources alongside the course material.

In perticular I studied Django using books written by William S. Vincent.

I began with his beginner-level Django material to strengthen my

understanding of Django fundamentals before progressing to his more

advanced material.

was aimed at beginners and helped me strengthen my understanding of

the fundamentals of Django development. I then progressed to a second,

more advanced Django book, which helped me develop my understanding

further.

I also used the official documentation for technologies used within

the project, including Django, Bootstrap, Stripe and FullCalendar.

### AI Assistance

ChatGPT was used as a learning and development aid during this project.

It was used to help explain Django concepts, troubleshoot errors, and review code.

---

## Author

**Dean Lark**

Created as part of the Code Institute Full Stack Development Diploma.