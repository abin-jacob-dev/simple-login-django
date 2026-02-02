Django Login System
===================

Project Overview
----------------

This project demonstrates a **simple user authentication system** using Django's built-in authentication system. The features include:

*   **Login Page**: Users can log in using their username and password.
    
*   **Logout Functionality**: Users can log out when they're done.
    
*   **Protected Home Page**: After logging in, users are redirected to a dashboard (home page) that requires authentication.
    
*   **Session-based Authentication**: User sessions are managed through Django’s built-in session management system.
    

Features
--------

*   **Login Page**: Allows users to enter their credentials (username and password).
    
*   **Logout Functionality**: Users can log out to end their session.
    
*   **Protected Home Page**: After successful login, users are redirected to a protected home page where they can view a personalized welcome message.
    
*   **Session Authentication**: The app uses Django’s session management to track logged-in users.
    

Project Structure
-----------------

The project follows Django's standard structure. Below is an overview of the key directories and files:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   abin-jacob-dev-simple-login-django/  ├── manage.py              # Main script for running server and administrative tasks  ├── accounts/              # Application for handling user authentication  │   ├── __init__.py        # Marks the directory as a Python package  │   ├── admin.py           # Django admin configuration (currently empty)  │   ├── apps.py            # App configuration file  │   ├── models.py          # Database models (currently empty)  │   ├── tests.py           # Test cases (currently empty)  │   ├── urls.py            # URL routing for authentication views  │   ├── views.py           # Views for handling authentication logic  │   └── templates/         # HTML templates for login, logout, and home pages  │       └── accounts/  │           ├── home.html  # Template for the home page (protected)  │           ├── login.html # Template for the login page  │           └── name.html  # Template for showing the username  └── simple_login/          # Main project folder      ├── __init__.py        # Marks the directory as a Python package      ├── asgi.py            # ASGI configuration for asynchronous support      ├── settings.py        # Django project settings      ├── urls.py            # Main URL configuration for the project      └── wsgi.py            # WSGI configuration for deployment   `

Tech Stack
----------

*   **Python**: Programming language used for the backend.
    
*   **Django**: Web framework that powers the backend logic and handles the authentication system.
    
*   **HTML / CSS**: For building the front-end templates and styling the pages.
    

How to Run the Project
----------------------

### Step 1: Clone the Repository

First, clone the repository to your local machine:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   git clone https://github.com/abin-jacob-dev/simple-login-django.git  cd simple-login-django   `

### Step 2: Set Up a Virtual Environment

Create a virtual environment to isolate project dependencies:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   # Create a virtual environment  python3 -m venv venv  # Activate the virtual environment  # On Windows  venv\Scripts\activate  # On Mac/Linux  source venv/bin/activate   `

### Step 3: Install Dependencies

Install the required dependencies using pip:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install -r requirements.txt   `

If the requirements.txt file doesn't exist, you can manually install Django using:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   pip install django   `

### Step 4: Run Migrations

Django uses a database to manage user authentication. Run migrations to set up the database:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python manage.py migrate   `

### Step 5: Create a Superuser (Admin Account)

To manage users and access the Django admin panel, create a superuser:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python manage.py createsuperuser   `

Follow the prompts to set up the superuser's username, email, and password.

### Step 6: Run the Server

Start the development server to see the application in action:

Plain textANTLR4BashCC#CSSCoffeeScriptCMakeDartDjangoDockerEJSErlangGitGoGraphQLGroovyHTMLJavaJavaScriptJSONJSXKotlinLaTeXLessLuaMakefileMarkdownMATLABMarkupObjective-CPerlPHPPowerShell.propertiesProtocol BuffersPythonRRubySass (Sass)Sass (Scss)SchemeSQLShellSwiftSVGTSXTypeScriptWebAssemblyYAMLXML`   python manage.py runserver   `

Your application will be available at http://127.0.0.1:8000/ in your browser.

Project Features
----------------

### 1\. **Login Page**

*   Users can log in with their username and password.
    
*   If the credentials are incorrect, an error message is displayed.
    

### 2\. **Logout Functionality**

*   After logging in, users can log out from the home page.
    

### 3\. **Protected Home Page**

*   Once logged in, users are redirected to a personalized dashboard where they can see a welcome message.
    

### 4\. **Session-based Authentication**

*   The app uses Django's authentication system to maintain user sessions. Once logged in, users stay logged in until they explicitly log out.
    

How the Code Works
------------------

### Views

1.  **login\_view**:
    
    *   Handles user login. If the user is already logged in, it redirects to the home page. Otherwise, it processes the login form and authenticates the user.
        
2.  **logout\_view**:
    
    *   Logs out the user and redirects them to the login page.
        
3.  **home**:
    
    *   A protected page that only authenticated users can access. It displays a personalized welcome message with the user's first name (if available).
        
4.  **name\_view**:
    
    *   Renders a simple template showing a static message (Abin Jacob).
        

### Templates

*   **home.html**: Displays the dashboard after the user logs in. Shows a personalized welcome message and a logout button.
    
*   **login.html**: The login form that allows the user to input their username and password.
    
*   **name.html**: Displays a static message (useful for testing purposes).
    

Helpful Links
-------------

*   **Django Documentation**: [https://docs.djangoproject.com/en/6.0/](https://docs.djangoproject.com/en/6.0/)
    
*   **Django Authentication System**: [https://docs.djangoproject.com/en/6.0/topics/auth/](https://docs.djangoproject.com/en/6.0/topics/auth/)
    

License
-------

This project is open-source and available under the MIT License.

Feel free to reach out if you have any questions or need further assistance!

This documentation should be easy to follow for beginners. It explains every aspect of the project from setup to execution. Let me know if you need to add more details!
