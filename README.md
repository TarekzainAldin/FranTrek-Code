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

### Clone the Repository
Clone the project repository to your local machine:
```bash
git clone https://github.com/TarekzainAldin/FranTrek-Code.git
cd FranTrek-Code
```

Create a Virtual Environment
It is recommended to use a virtual environment for dependency management:

bash
Copy code
python -m venv venv
Activate the virtual environment:

On macOS/Linux:
bash
Copy code
source venv/bin/activate
On Windows:
bash
Copy code
venv\Scripts\activate
Install Dependencies
With the virtual environment activated, install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set Up Environment Variables
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

Database Migration
Initialize and migrate the database:

bash
Copy code
flask db init
flask db migrate
flask db upgrade
Run the Application
Start the application:

bash
Copy code
flask run
Visit http://127.0.0.1:5000 in your browser to view the application.
##Folder Structure
