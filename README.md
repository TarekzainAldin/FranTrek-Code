<p class="has-line-data" data-line-start="0" data-line-end="2">FranTrek-Code<br>
FranTrek-Code is a Flask-based web application designed to manage and administer courses and lessons efficiently. The project features user authentication, a content management system, a RESTful API for managing data, and an admin dashboard for administration.</p>
<p class="has-line-data" data-line-start="3" data-line-end="17">Table of Contents<br>
Project Overview<br>
Technologies Used<br>
Setup Instructions<br>
Folder Structure<br>
Features<br>
Usage<br>
API Endpoints<br>
Future Enhancements<br>
Contributing<br>
License<br>
Acknowledgments<br>
Project Overview<br>
FranTrek-Code is a learning management system that allows instructors to create and manage courses and lessons. Users can register, log in, view course content, and receive notifications for lesson updates. The project uses Flask for the backend and integrates several extensions for enhanced functionality.</p>
<p class="has-line-data" data-line-start="18" data-line-end="46">Technologies Used<br>
Backend Framework: Flask<br>
Database: SQLAlchemy (with Flask-Migrate for database migrations)<br>
Authentication: Flask-Login, Flask-Bcrypt<br>
Admin Interface: Flask-Admin<br>
API Management: Flask-Cors, RESTful Blueprints<br>
Rich Text Editing: Flask-CKEditor<br>
Email Handling: Flask-Mail<br>
Frontend: Jinja2 Templates<br>
Other Libraries: WTForms, Pillow (for image handling), Mako, Alembic<br>
Setup Instructions<br>
Clone the Repository<br>
bash<br>
Copy code<br>
git clone <a href="https://github.com/TarekzainAldin/FranTrek-Code.git">https://github.com/TarekzainAldin/FranTrek-Code.git</a><br>
cd FranTrek-Code<br>
Create a Virtual Environment<br>
bash<br>
Copy code<br>
python -m venv venv<br>
source venv/bin/activate  # On macOS/Linux<br>
venv\Scripts\activate     # On Windows<br>
Install Dependencies<br>
bash<br>
Copy code<br>
pip install -r requirements.txt<br>
Set Up Environment Variables<br>
Create a .env file in the root directory and add the following:</p>
<p class="has-line-data" data-line-start="47" data-line-end="69">env<br>
Copy code<br>
FLASK_APP=<a href="http://run.py">run.py</a><br>
FLASK_ENV=development<br>
SECRET_KEY=your_secret_key<br>
SQLALCHEMY_DATABASE_URI=sqlite:///site.db<br>
MAIL_SERVER=<a href="http://smtp.yourmailserver.com">smtp.yourmailserver.com</a><br>
MAIL_PORT=587<br>
MAIL_USE_TLS=True<br>
MAIL_USERNAME=your_email<br>
MAIL_PASSWORD=your_email_password<br>
Database Migration<br>
bash<br>
Copy code<br>
flask db init<br>
flask db migrate<br>
flask db upgrade<br>
Run the Application<br>
bash<br>
Copy code<br>
flask run<br>
Visit <a href="http://127.0.0.1:5000">http://127.0.0.1:5000</a> to see the application in action.</p>
<p class="has-line-data" data-line-start="70" data-line-end="121">Folder Structure<br>
markdown<br>
Copy code<br>
FranTrek-Code/<br>
│<br>
├── FranTrek/<br>
│   ├── <strong>init</strong>.py<br>
│   ├── <a href="http://config.py">config.py</a><br>
│   ├── <a href="http://models.py">models.py</a><br>
│   ├── adminbp/<br>
│   │   ├── <strong>init</strong>.py<br>
│   │   └── <a href="http://routes.py">routes.py</a><br>
│   ├── main/<br>
│   │   ├── <strong>init</strong>.py<br>
│   │   └── <a href="http://routes.py">routes.py</a><br>
│   ├── users/<br>
│   │   ├── <strong>init</strong>.py<br>
│   │   ├── <a href="http://routes.py">routes.py</a><br>
│   │   └── user_api.py<br>
│   ├── courses/<br>
│   │   ├── <strong>init</strong>.py<br>
│   │   ├── <a href="http://routes.py">routes.py</a><br>
│   │   └── courses_api.py<br>
│   └── errors/<br>
│       ├── <strong>init</strong>.py<br>
│       └── <a href="http://handlers.py">handlers.py</a><br>
│<br>
├── migrations/<br>
├── static/<br>
├── templates/<br>
├── .env<br>
├── requirements.txt<br>
└── <a href="http://run.py">run.py</a><br>
Features<br>
User Authentication: Registration, login, password reset via email, and user profile management.<br>
Admin Dashboard: Manage users, courses, and lessons through a rich interface.<br>
Course and Lesson Management: Create, update, and delete courses and lessons with a built-in text editor.<br>
RESTful API: Manage and fetch data through secure and structured endpoints.<br>
Email Notifications: Automated email services for password resets and updates.<br>
Modal Support: Rich UI modals using Flask-Modals.<br>
Cross-Origin Resource Sharing: Enabled through Flask-Cors for API access.<br>
Usage<br>
User Authentication: Users can register and log in. Profiles can be edited, and passwords can be reset via email.<br>
Admin Interface: Admin users can manage site content, including courses and lessons.<br>
Course Access: Users can browse and view lessons, complete with thumbnails and content.<br>
Interactive API: Use tools like Postman to test the API endpoints.<br>
API Endpoints<br>
User API: /api/users<br>
Lesson API: /api/lessons<br>
Course API: /api/courses<br>
For detailed API documentation, refer to the project’s API docs or check the user_api.py, lessons_api.py, and courses_api.py files.</p>
<p class="has-line-data" data-line-start="122" data-line-end="135">Future Enhancements<br>
Role-Based Access Control: Different permissions for instructors and students.<br>
Enhanced UI: Modern front-end technologies like React or Vue.js for a richer user experience.<br>
Mobile Support: Responsive design for better mobile accessibility.<br>
Additional Analytics: Track user engagement and course completion rates.<br>
Contributing<br>
Fork the Project.<br>
Create a Feature Branch: git checkout -b feature-name.<br>
Commit Your Changes: git commit -m ‘Add new feature’.<br>
Push to the Branch: git push origin feature-name.<br>
Open a Pull Request.<br>
License<br>
This project is licensed under the MIT L