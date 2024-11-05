from flask import Blueprint, jsonify, request, url_for
from FranTrek.models import User
from FranTrek.users.forms import RegistrationForm
from FranTrek import bcrypt, db
from flask_login import login_required, login_user, current_user, logout_user
from FranTrek.helpers import save_picture
from FranTrek.users.helpers import send_reset_email

users_api = Blueprint("users_api", __name__)

@users_api.route("/register", methods=["POST"])
def api_register():
    data = request.get_json()
    form = RegistrationForm(data)
    if form.validate_on_submit():  # Change this to match the form validation method
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf-8")
        user = User(
            fname=form.fname.data,
            lname=form.lname.data,
            username=form.username.data,
            email=form.email.data,
            password=hashed_password,
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({"message": f"Account created successfully for {form.username.data}"}), 201
    return jsonify({"errors": form.errors}), 400

@users_api.route("/login", methods=["POST"])
def api_login():
    data = request.get_json()
    user = User.query.filter_by(email=data.get("email")).first()
    if user and bcrypt.check_password_hash(user.password, data.get("password")):
        login_user(user, remember=data.get("remember", False))
        return jsonify({"message": "Login successful", "username": user.username}), 200
    return jsonify({"message": "Login Unsuccessful. Please check credentials"}), 401

@users_api.route("/logout", methods=["POST"])
@login_required
def api_logout():
    logout_user()
    return jsonify({"message": "Logout successful"}), 200

@users_api.route("/profile", methods=["GET", "PUT"])
@login_required
def api_profile():
    if request.method == "PUT":
        data = request.get_json()
        if data.get("picture"):
            picture_file = save_picture(data["picture"], "static/user_pics", output=(150, 150))
            current_user.image_file = picture_file
        current_user.username = data.get("username", current_user.username)
        current_user.email = data.get("email", current_user.email)
        current_user.bio = data.get("bio", current_user.bio)
        db.session.commit()
        return jsonify({"message": "Your profile has been updated"}), 200
    profile_data = {
        "username": current_user.username,
        "email": current_user.email,
        "bio": current_user.bio,
        "image_file": url_for("static", filename=f"user_pics/{current_user.image_file}")
    }
    return jsonify(profile_data), 200

@users_api.route("/reset_password", methods=["POST"])
def api_reset_request():
    data = request.get_json()
    user = User.query.filter_by(email=data.get("email")).first()
    if user:
        send_reset_email(user)
    return jsonify({"message": "If this account exists, you will receive an email with instructions"}), 200

@users_api.route("/reset_password/<token>", methods=["POST"])
def api_reset_password(token):
    user = User.verify_reset_token(token)
    if not user:
        return jsonify({"message": "The token is invalid or expired"}), 400
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data.get("password")).decode("utf-8")
    user.password = hashed_password
    db.session.commit()
    return jsonify({"message": "Your password has been updated. You can now log in"}), 200
