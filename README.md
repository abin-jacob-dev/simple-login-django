

# Django Login System

A simple user authentication system built using **Django’s built-in authentication framework**.  
This project demonstrates login, logout, protected routes, and session-based authentication.

---

## Features

- User login with username and password  
- User logout functionality  
- Protected home (dashboard) page  
- Session-based authentication using Django  

---

## Tech Stack

- **Python**
- **Django**
- **HTML / CSS**

---

## Project Structure


```
simple-login-django/
├── manage.py
├── accounts/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   └── templates/
│       └── accounts/
│           ├── home.html
│           ├── login.html
│           └── name.html
└── simple_login/
├── **init**.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py

````

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/abin-jacob-dev/simple-login-django.git
cd simple-login-django
````

### 2. Create and Activate Virtual Environment

```bash
python3 -m venv venv
```

**Activate:**

* Windows:

```bash
venv\Scripts\activate
```

* Mac / Linux:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django
```

> If `requirements.txt` exists:

```bash
pip install -r requirements.txt
```

### 4. Run Migrations

```bash
python manage.py migrate
```

### 5. Create Superuser

```bash
python manage.py createsuperuser
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Open your browser and go to:
👉 `http://127.0.0.1:8000/`

---

## Application Pages

### Login Page

* Users log in using username and password
* Shows error message on invalid credentials

### Home Page (Protected)

* Accessible only after login
* Displays a personalized welcome message

### Logout

* Ends the user session and redirects to login page

---

## Views Overview

* **login_view**
  Handles authentication and redirects logged-in users to home.

* **logout_view**
  Logs out the user and redirects to login page.

* **home**
  Protected dashboard view for authenticated users only.

* **name_view**
  Displays a static name message (for testing/demo).

---

## Templates

* `login.html` – Login form
* `home.html` – Dashboard page
* `name.html` – Static display page

---

## Useful Links

* Django Docs: [https://docs.djangoproject.com/en/6.0/](https://docs.djangoproject.com/en/6.0/)
* Django Auth System: [https://docs.djangoproject.com/en/6.0/topics/auth/](https://docs.djangoproject.com/en/6.0/topics/auth/)

---

## License

This project is licensed under the **MIT License**.

```

---

If you want, I can also:
- ✨ Make it **more GitHub-professional**
- 📦 Add **screenshots section**
- 🔐 Add **signup / password reset**
- 🧪 Add **tests**
- 🚀 Prepare it for **deployment**

Just tell me 😄
```
