# FranTrek-Code

FranTrek-Code is a Flask-based web application designed to manage courses and lessons. It includes user authentication, a content management system, a RESTful API for data management, and an admin dashboard for administration.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Folder Structure](#folder-structure)
- [Features](#features)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)
- [GitHub Repository](#github-repository)

## Project Overview
FranTrek-Code is a learning management system (LMS) that enables instructors to create, manage, and administer courses and lessons. It allows users to register, log in, view lessons, and receive updates via email. Built with Flask, the application integrates several extensions for enhanced functionality and includes a RESTful API for external systems to interact with course and lesson data.

## Technologies Used
- **Backend Framework**: Flask
- **Database**: SQLAlchemy (with Flask-Migrate for migrations)
- **Authentication**: Flask-Login, Flask-Bcrypt
- **Admin Interface**: Flask-Admin
- **API Management**: Flask-Cors, RESTful Blueprints
- **Rich Text Editing**: Flask-CKEditor
- **Email Handling**: Flask-Mail
- **Frontend**: Jinja2 Templates
- **Other Libraries**: Alembic, bcrypt, Flask-WTF, WTForms, Pillow, Mako, Flask-Modals, and more.

## Setup Instructions

### 1. Clone the Repository
To begin, clone the project repository to your local machine:
```bash
git clone https://github.com/TarekzainAldin/FranTrek-Code.git
cd FranTrek-Code
2. Create a Virtual Environment
It is recommended to use a virtual environment for dependency management:

bash
Copy code
python -m venv venv
3. Activate the Virtual Environment
On macOS/Linux:
bash
Copy code
source venv/bin/activate
On Windows:
bash
Copy code
venv\Scripts\activate
4. Install Dependencies
With the virtual environment activated, install the required dependencies:

bash
Copy code
pip install -r requirements.txt
5. Set Up Environment Variables
Create a .env file in the root directory and add the following environment variables:

ini
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
Replace your_secret_key, your_email, and your_email_password with actual values.

6. Database Migration
Initialize and migrate the database:

bash
Copy code
flask db init
flask db migrate
flask db upgrade
7. Run the Application
Start the application:

bash
Copy code
flask run
Visit http://127.0.0.1:5000 in your browser to view the application.

Folder Structure
The project’s folder structure is as follows:

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
User Authentication: Allows users to register, log in, reset passwords via email, and manage profiles.
Admin Dashboard: Admins can manage users, courses, and lessons through an intuitive interface.
Course & Lesson Management: Instructors can create, update, and delete courses and lessons using a rich text editor.
RESTful API: Secure API endpoints for interacting with user, course, and lesson data.
Email Notifications: Automated email notifications for password resets and updates.
Modal Support: Rich modals for user interactions via Flask-Modals.
CORS Support: Enabled through Flask-Cors for external API access.
Usage
User Authentication: Users can register, log in, and reset passwords.
Admin Interface: Admin users can manage courses, lessons, and users.
Course Access: Students can browse and view lessons.
Interactive API: Test API endpoints using tools like Postman.
API Endpoints
The following API endpoints are available:

User API: /api/users
Lesson API: /api/lessons
Course API: /api/courses
For detailed API documentation, refer to the user_api.py, lessons_api.py, and courses_api.py files in the project.

Future Enhancements
Role-Based Access Control: Implement permissions for instructors and students.
Enhanced UI: Upgrade to modern front-end frameworks like React or Vue.js for a richer user experience.
Mobile Support: Make the application mobile-responsive.
Analytics: Track user engagement and course completion rates.
Contributing
To contribute to FranTrek-Code:

Fork the Project: Create a personal copy of the repository.
Create a Feature Branch:
bash
Copy code
git checkout -b feature-name
Commit Your Changes:
bash
Copy code
git commit -m 'Add new feature'
Push to the Branch:
bash
Copy code
git push origin feature-name
Open a Pull Request: Submit a pull request from your feature branch to the main repository.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Special thanks to the Flask framework and community for their support and tools, as well as the various libraries, including SQLAlchemy, Flask-Admin, Flask-Login, and others used in this project.

GitHub Repository
Find the project on GitHub: FranTrek-Code GitHub Repository
