# FitRoutine Project

FitRoutine is a web application built with Django that allows users to register, log in, and manage their workout routines. The application provides features for creating, editing, and deleting personalized workout routines, tracking body parameters, and accessing a manual with exercise documentation and nutritional information.

## Features

- User registration and login with email verification and password reset functionality.
- Ability to create, edit, and delete custom workout routines.
- Selection of exercises based on targeted muscle groups.
- Tracking of body parameters such as weight, height, and measurements.
- Access to a manual with categorized exercise documentation and nutritional information.

## Technologies Used

- Django: A high-level Python web framework for rapid development.
- PostgreSQL: A powerful, open-source object-relational database system.
- HTML/CSS: For front-end development and user interface design.

## Project Structure

```
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
└── db.sqlite3
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd FitRoutine
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
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

8. Access the application at `http://127.0.0.1:8000/`.

## Future Enhancements

- Extend the application to support mobile platforms using Django Rest Framework.
- Implement additional features based on user feedback.

## License

This project is licensed under the MIT License.