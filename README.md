# FranTrek-Code

**FranTrek-Code** is a Flask-based web application designed to manage and administer courses and lessons efficiently. The project features user authentication, a content management system, a RESTful API for managing data, and an admin dashboard for administration.

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Folder Structure](#folder-structure)
5. [Features](#features)
6. [Usage](#usage)
7. [API Endpoints](#api-endpoints)
8. [Future Enhancements](#future-enhancements)
9. [Contributing](#contributing)
10. [License](#license)
11. [Acknowledgments](#acknowledgments)

---

## Project Overview
FranTrek-Code is a learning management system that allows instructors to create and manage courses and lessons. Users can register, log in, view course content, and receive notifications for lesson updates. The project uses Flask for the backend and integrates several extensions for enhanced functionality.

---

## Technologies Used
- **Backend Framework**: Flask
- **Database**: SQLAlchemy (with Flask-Migrate for database migrations)
- **Authentication**: Flask-Login, Flask-Bcrypt
- **Admin Interface**: Flask-Admin
- **API Management**: Flask-Cors, RESTful Blueprints
- **Rich Text Editing**: Flask-CKEditor
- **Email Handling**: Flask-Mail
- **Frontend**: Jinja2 Templates
- **Other Libraries**: WTForms, Pillow (for image handling), Mako, Alembic

---

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/TarekzainAldin/FranTrek-Code.git
cd FranTrek-Code
Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
Install Dependencies
bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables
Create a .env file in the root directory and add the following:

env
Copy code
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your_secret_key
SQLALCHEMY_DATABASE_URI=sqlite:///site.db
MAIL_SERVER=smtp.yourmailserver.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your_email
MAIL_PASSWORD=your_email_password
Database Migration
bash
Copy code
flask db init
flask db migrate
flask db upgrade
Run the Application
bash
Copy code
flask run
Visit http://127.0.0.1:5000 to see the application in action.


## Folder Structure
Folder Structure
markdown
Copy code
FranTrek-Code/
│
├── FranTrek/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── adminbp/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── main/
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── users/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── user_api.py
│   ├── courses/
│   │   ├── __init__.py
│   │   ├── routes.py
│   │   └── courses_api.py
│   └── errors/
│       ├── __init__.py
│       └── handlers.py
│
├── migrations/
├── static/
├── templates/
├── .env
├── requirements.txt
└── run.py
Features
User Authentication: Registration, login, password reset via email, and user profile management.
Admin Dashboard: Manage users, courses, and lessons through a rich interface.
Course and Lesson Management: Create, update, and delete courses and lessons with a built-in text editor.
RESTful API: Manage and fetch data through secure and structured endpoints.
Email Notifications: Automated email services for password resets and updates.
Modal Support: Rich UI modals using Flask-Modals.
Cross-Origin Resource Sharing: Enabled through Flask-Cors for API access.
Usage
User Authentication: Users can register and log in. Profiles can be edited, and passwords can be reset via email.
Admin Interface: Admin users can manage site content, including courses and lessons.
Course Access: Users can browse and view lessons, complete with thumbnails and content.
Interactive API: Use tools like Postman to test the API endpoints.
API Endpoints
User API: /api/users
Lesson API: /api/lessons
Course API: /api/courses
For detailed API documentation, refer to the project’s API docs or check the user_api.py, lessons_api.py, and courses_api.py files.

Future Enhancements
Role-Based Access Control: Different permissions for instructors and students.
Enhanced UI: Modern front-end technologies like React or Vue.js for a richer user experience.
Mobile Support: Responsive design for better mobile accessibility.
Additional Analytics: Track user engagement and course completion rates.
Contributing
Fork the Project.
Create a Feature Branch: git checkout -b feature-name.
Commit Your Changes: git commit -m 'Add new feature'.
Push to the Branch: git push origin feature-name.
Open a Pull Request.
