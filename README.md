# FitRoutine Project

FitRoutine is a web application built with Django that allows users to register, log in, and manage their workout routines. Provides features for creating, editing, and deleting personalized workout routines, tracking body parameters, and accessing a manual with exercise documentation and nutritional information.

## Features

- User registration and login with email verification and password reset functionality.
- Ability to create, edit, and delete custom workout routines.
- Selection of exercises based on targeted muscle groups.
- Tracking of body parameters such as weight, height, and measurements.
- Access to a manual with categorized exercise documentation and nutritional information.

## Technologies Used

- Django - Python
- PostgreSQL
- HTML/CSS

## Project Structure

FitRoutine
├── fitroutine
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   ├── asgi.py
│   └── templates
│       ├── base.html
│       ├── registration
│       │   ├── login.html
│       │   ├── register.html
│       │   ├── password_reset.html
│       │   ├── password_reset_done.html
│       │   ├── password_reset_confirm.html
│       │   └── password_reset_complete.html
│       └── workouts
│           ├── create_workout.html
│           ├── edit_workout.html
│           ├── delete_workout.html
│           └── workouts.html
├── users
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates
│       └── users
│           ├── profile.html
│           └── update_profile.html
├── workouts
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates
│       └── workouts
│           ├── create_workout.html
│           ├── edit_workout.html
│           ├── delete_workout.html
│           └── workouts.html
├── manual
│   ├── __init__.py
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates
│       └── manual
│           ├── exercises.html
│           ├── nutrition.html
│           └── encyclopedia.html
├── manage.py
├── requirements.txt

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd FitRoutine
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/Scripts/activate 
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Configure the PostgreSQL database in `settings.py`.

5. Run database migrations:
   ```
   python manage.py migrate
   ```

6. Create a superuser to access the admin interface:
   ```
   python manage.py createsuperuser
   ```

7. Start the development server:
   ```
   python manage.py runserver
   ```

