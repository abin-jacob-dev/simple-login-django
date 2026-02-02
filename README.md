# Django Login System

## Project Overview

This project demonstrates a **simple user authentication system** using Django's built-in authentication system. The features include:

- **Login Page**: Users can log in with their username and password.
- **Logout Functionality**: Users can log out when they're done.
- **Protected Home Page**: After logging in, users are redirected to a dashboard that requires authentication.
- **Session-based Authentication**: User sessions are managed through Django’s session management system.

## Features

- **Login Page**: Allows users to enter their credentials (username and password).
- **Logout Functionality**: Users can log out to end their session.
- **Protected Home Page**: After logging in, users are redirected to a protected home page with a personalized welcome message.
- **Session Authentication**: The app uses Django’s session management to track logged-in users.

## Project Structure

The project follows Django's standard structure. Key files and directories include:

```
abin-jacob-dev-simple-login-django/
├── manage.py              # Main script for running server and administrative tasks
├── accounts/              # Application for user authentication
│   ├── __init__.py        # Marks the directory as a Python package
│   ├── admin.py           # Django admin configuration (currently empty)
│   ├── apps.py            # App configuration file
│   ├── models.py          # Database models (currently empty)
│   ├── tests.py           # Test cases (currently empty)
│   ├── urls.py            # URL routing for authentication views
│   ├── views.py           # Views for authentication logic
│   └── templates/         # HTML templates for login, logout, and home pages
│       └── accounts/
│           ├── home.html  # Template for the home page (protected)
│           ├── login.html # Template for the login page
│           └── name.html  # Template for showing the username
└── simple_login/          # Main project folder
├── __init__.py        # Marks the directory as a Python package
├── asgi.py            # ASGI configuration for asynchronous support
├── settings.py        # Django project settings
├── urls.py            # Main URL configuration for the project
└── wsgi.py            # WSGI configuration for deployment
```

## Tech Stack
- **Python**: Backend programming language.
- **Django**: Web framework for handling authentication and other backend logic.
- **HTML / CSS**: Used for building and styling front-end templates.

## How to Run the Project
### Step 1: Clone the Repository
to clone the repository:
```bash
git clone https://github.com/abin-jacob-dev/simple-login-django.git
dc simple-login-django
def clone_the_repository():
    pass  
``` 
define this function accordingly or run these commands manually. 
### Step 2: Set Up a Virtual Environment
to create and activate a virtual environment:
```bash# Create a virtual environmentpython3 -m venv venv# Activate on Windowsvenv\Scripts\activate# Activate on Mac/Linuxsource venv/bin/activate``` 
define this function accordingly or run these commands manually. 
### Step 3: Install Dependencies
to install dependencies:
```bashpip install -r requirements.txt```
or install Django manually if `requirements.txt` is missing:
pip install django 
define this function accordingly or run these commands manually. 
### Step 4: Run Migrations
to set up database:
def migrate_database():
    import os; os.system('python manage.py migrate')
define this function accordingly or run this command manually. 
### Step 5: Create a Superuser (Admin Account)
to create an admin user:
def create_superuser():
    import os; os.system('python manage.py createsuperuser')
define this function accordingly or run this command manually. 
### Step 6: Run the Server
to start server:
def start_server():
    import os; os.system('python manage.py runserver')
define this function accordingly or run this command manually. 
your application will be available at `http://127.0.0.1:8000/` in your browser.
## Project Features
### 1. **Login Page**
specifics about login page...
and so on.
