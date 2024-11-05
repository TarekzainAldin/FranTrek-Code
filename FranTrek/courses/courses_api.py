# FranTrek/courses/courses_api.py
from flask import Blueprint, jsonify, request, abort
from FranTrek.models import Course, Lesson
from FranTrek import db

# Initialize Blueprint for the Courses API
courses_api = Blueprint("courses_api", __name__)

@courses_api.route("/courses", methods=["GET"])
def get_courses():
    """Get a paginated list of courses."""
    page = request.args.get("page", 1, type=int)
    courses = Course.query.paginate(page=page, per_page=6)
    
    courses_data = [
        {
            "id": course.id,
            "title": course.title,
            "description": course.description,  # Assuming you have a description field
            # Include any other fields you want to expose
        }
        for course in courses.items  # Use items for the current page's courses
    ]
    
    return jsonify({
        "courses": courses_data,
        "has_next": courses.has_next,
        "has_prev": courses.has_prev,
        "total": courses.total,
        "page": courses.page
    })

@courses_api.route("/courses/<string:course_title>", methods=["GET"])
def get_course(course_title):
    """Get a specific course by title along with its lessons."""
    course = Course.query.filter_by(title=course_title).first()
    if not course:
        abort(404, "Course not found.")

    # Fetch lessons associated with the course
    lessons = Lesson.query.filter_by(course_id=course.id).all()
    
    lessons_data = [
        {
            "id": lesson.id,
            "title": lesson.title,
            "content": lesson.content,
            "slug": lesson.slug,
            # Add any other fields you want to include
        }
        for lesson in lessons
    ]
    
    course_data = {
        "id": course.id,
        "title": course.title,
        "description": course.description,  # Assuming you have a description field
        "lessons": lessons_data
    }

    return jsonify(course_data)
