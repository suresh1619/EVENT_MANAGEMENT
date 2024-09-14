# EVENT_MANAGEMENT
Overview
This project is a Django-based event management system with user authentication features. It includes functionalities for user registration and login, as well as basic event management operations such as creating, viewing, updating, and deleting events.

Features
User Authentication: Allows users to sign up, log in, and access event details.
Event Management: Users can create, view, update, and delete events.
Responsive Design: HTML templates are styled with CSS for a better user experience.
Requirements
Ensure you have the following installed:

Python 3.x
Django
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-repository-url.git
Navigate to the Project Directory:

bash
Copy code
cd your-project-directory
Create a Virtual Environment:

bash
Copy code
python -m venv venv
Activate the Virtual Environment:

On Windows:
bash
Copy code
venv\Scripts\activate
On macOS/Linux:
bash
Copy code
source venv/bin/activate
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Apply Migrations:

bash
Copy code
python manage.py migrate
Create a Superuser (optional, for admin access):

bash
Copy code
python manage.py createsuperuser
Run the Development Server:

bash
Copy code
python manage.py runserver
Access the Application: Open your web browser and go to http://127.0.0.1:8000/.

Usage
User Registration
Navigate to the signup page (/signup/).
Fill out the registration form and submit.
User Login
Navigate to the login page (/login/).
Enter your username and password to log in.
Event Management
Once logged in, users can access event details and perform various event management tasks.

Code Explanation
Views
login(request): Handles user authentication. Checks the provided username and password against the Signup model and redirects to the event details page on success.

signup(request): Handles user registration. Saves user details to the Signup model.

home(request): Renders the home page.

Templates
login.html: Template for user login.
signup.html: Template for user registration.


event-management-system/
│
├── events/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   └── urls.py
│
├── event-management-system/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
|_static
|
|_  templates

