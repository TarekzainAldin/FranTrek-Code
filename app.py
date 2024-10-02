from flask import Flask, render_template, url_for ,flash,redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy 
from form import RegistrationForm, LoginForm
app = Flask(__name__)
app.config[
    "SECRET_KEY"
] = '16c749724f0c2920edea51b1b4e7af80f9a10f2ed97981830c0c9109f2370862'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///FranTrek.db'

db=SQLAlchemy(app)
app.app_context().push()

lessons = [{
    'title': 'Request Library Course',
    'course': 'Python',
    'author': 'tarek',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'tarek',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'francia',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'francia',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'francia',
    'thumbnail': 'thumbnail.jpg'
},
{'title': 'Request Library Course',
    'course': 'Python',
    'author': 'tarek',
    'thumbnail': 'thumbnail.jpg'
},
]

courses = [
{
        'name': 'Python',
        'icon': 'python.svg',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

    {
        'name': 'Data Analysis',
        'icon': 'analysis.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

    {
        'name': 'Machine Learning',
        'icon': 'machine-learning.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Web Design',
        'icon': 'web.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Blockchain',
        'icon': 'blockchain.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

        {
        'name': 'Tips & Tricks',
        'icon': 'idea.png',
        'description': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Neque quidem nihil dolor officiis at magni!'
    },

]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', lessons=lessons, courses=courses)

@app.route("/about")
def about():
    return render_template('about.html', title="About")


@app.route("/register", methods=["GET", "POST"])

def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created successfully for {form.username.data}", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if (
            form.email.data == "tarek@gmail.com"
            and form.password.data == "T123!!@tt"
        ):
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check credentials", "danger")
    return render_template("login.html", title="Login", form=form)




class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(25), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(125), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.jpg")
    password = db.Column(db.String(60), nullable=False)
    lessons = db.relationship("Lesson", backref="author", lazy=True)

    def __repr__(self):
        return f"User('{self.fname}', '{self.lname}', '{self.username}', '{self.email}', '{self.image_file}')"


class Lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    thumbnail = db.Column(
        db.String(20), nullable=False, default="default_thumbnail.jpg"
    )
    slug = db.Column(db.String(32), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey("course.id"), nullable=False)

    def __repr__(self):
        return f"Lesson('{self.title}', '{self.date_posted}')"


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(150), nullable=False)
    icon = db.Column(db.String(20), nullable=False, default="default_icon.jpg")
    lessons = db.relationship("Lesson", backref="course_name", lazy=True)

    def __repr__(self):
        return f"Course('{self.title}')"

if __name__ == "__main__":
    #   with app.app_context():  # Make sure to create an app context
    #    db.create_all()  
 app.run(debug=True) 