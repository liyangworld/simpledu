from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required

import requests

course = Blueprint('course', __name__, url_prefix='/courses')

@course.route('/')
def index():
    return render_template('courses/index.html')

@course.route('/<int:course_id>')
def detail(course_id):
    res = requests.get("http://localhost:5001/api/v1.0/courses/{0}".format(course_id), params=None)
    resData = res.json()
    if resData['Success']:
        return render_template('courses/detail.html', course=resData['data'])
    else:
        return render_template('errors/404.html'), 404



@course.route('/<int:course_id>/chapters/<int:chapter_id>')
@login_required
def chapter(course_id, chapter_id):
    url = "http://localhost:5001/api/v1.0/courses/{0}/chapters/{1}".format(course_id, chapter_id)
    res = requests.get(url, params=None)
    resData = res.json()
    if resData['Success']:
        return render_template('courses/chapter.html', chapter=resData['data'])
    else:
        return render_template('errors/404.html'), 404

