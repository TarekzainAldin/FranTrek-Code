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