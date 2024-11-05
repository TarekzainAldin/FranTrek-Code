# FranTrek/lessons/lessons_api.py
import os
import logging
from flask import Blueprint, jsonify, request, abort
from FranTrek.models import Lesson, Course
from FranTrek import db
from flask_login import current_user, login_required
from FranTrek.helpers import save_picture, delete_picture

# Initialize Blueprint for the Lessons API
lessons_api = Blueprint("lessons_api", __name__)

# Set up logging
logging.basicConfig(level=logging.INFO)

@lessons_api.route("/lessons", methods=["GET"])
def get_lessons():
    try:
        lessons = Lesson.query.all()
        lessons_data = [
            {
                "id": lesson.id,
                "title": lesson.title,
                "content": lesson.content,
                "slug": lesson.slug,
            }
            for lesson in lessons
        ]
        return jsonify(lessons_data)
    except Exception as e:
        logging.error(f"Error fetching lessons: {str(e)}")
        return jsonify({"error": "An internal error occurred while fetching lessons."}), 500

@lessons_api.route("/lessons/<int:lesson_id>", methods=["GET"])
def get_lesson(lesson_id):
    try:
        lesson = Lesson.query.get_or_404(lesson_id)
        lesson_data = {
            "id": lesson.id,
            "title": lesson.title,
            "content": lesson.content,
            "slug": lesson.slug,
            "author": lesson.author.username,
            "course_name": lesson.course_name,
        }
        return jsonify(lesson_data)
    except Exception as e:
        logging.error(f"Error fetching lesson {lesson_id}: {str(e)}")
        abort(500, "An error occurred while fetching the lesson.")

@lessons_api.route("/lessons", methods=["POST"])
@login_required
def create_lesson():
    try:
        data = request.get_json()
        if not data or "title" not in data or "content" not in data or "course_name" not in data:
            abort(400, "Missing required fields: title, content, or course_name.")

        lesson_slug = str(data.get("slug", data["title"])).replace(" ", "-")
        course_name = data["course_name"]

        # Check if course exists
        course = Course.query.filter_by(name=course_name).first()
        if not course:
            abort(404, "Course not found.")

        new_lesson = Lesson(
            title=data["title"],
            content=data["content"],
            slug=lesson_slug,
            author=current_user,
            course_name=course_name,
        )

        if "thumbnail" in data:
            picture_file = save_picture(data["thumbnail"], "static/lesson_thumbnails")
            new_lesson.thumbnail = picture_file

        db.session.add(new_lesson)
        db.session.commit()

        return jsonify({"message": "Lesson created successfully!", "lesson_id": new_lesson.id}), 201
    except Exception as e:
        logging.error(f"Error creating lesson: {str(e)}")
        abort(500, "An error occurred while creating the lesson.")

@lessons_api.route("/lessons/<int:lesson_id>", methods=["PUT"])
@login_required
def update_lesson_api(lesson_id):
    try:
        lesson = Lesson.query.get_or_404(lesson_id)
        if lesson.author != current_user:
            abort(403, "You do not have permission to edit this lesson.")

        data = request.get_json()
        lesson.title = data.get("title", lesson.title)
        lesson.content = data.get("content", lesson.content)
        lesson.slug = str(data.get("slug", lesson.slug)).replace(" ", "-")
        lesson.course_name = data.get("course_name", lesson.course_name)

        if "thumbnail" in data:
            delete_picture(lesson.thumbnail, "static/lesson_thumbnails")
            new_picture = save_picture(data["thumbnail"], "static/lesson_thumbnails")
            lesson.thumbnail = new_picture

        db.session.commit()
        return jsonify({"message": "Lesson updated successfully!"})
    except Exception as e:
        logging.error(f"Error updating lesson {lesson_id}: {str(e)}")
        abort(500, "An error occurred while updating the lesson.")

@lessons_api.route("/lessons/<int:lesson_id>", methods=["DELETE"])
@login_required
def delete_lesson_api(lesson_id):
    try:
        lesson = Lesson.query.get_or_404(lesson_id)
        if lesson.author != current_user:
            abort(403, "You do not have permission to delete this lesson.")

        db.session.delete(lesson)
        db.session.commit()
        return jsonify({"message": "Lesson deleted successfully!"})
    except Exception as e:
        logging.error(f"Error deleting lesson {lesson_id}: {str(e)}")
        abort(500, "An error occurred while deleting the lesson.")
