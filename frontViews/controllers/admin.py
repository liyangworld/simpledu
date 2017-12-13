from flask import Blueprint, render_template
from frontViews.decorators import admin_required

import requests

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')

@admin.route('/courses')
@admin_required
def courses():
    return render_template('admin/courses/courses.html')


@admin.route('/courses/create')
@admin_required
def create_course():
    return render_template('admin/courses/createCourse.html')

@admin.route('/courses/<int:course_id>/edit')
@admin_required
def edit_course(course_id):
    res = requests.get("http://localhost:5001/api/v1.0/courses/{0}".format(course_id), params=None)
    resData = res.json()
    if resData['Success']:
        return render_template('admin/courses/editCourse.html', course=resData['data'])
    else:
        return render_template('errors/404.html'), 404


@admin.route('/users')
@admin_required
def users():
    return render_template('admin/users/users.html')


@admin.route('/users/create')
@admin_required
def create_user():
    return render_template('admin/users/createUser.html')

@admin.route('/users/<int:user_id>/edit')
@admin_required
def edit_user(user_id):
    res = requests.get("http://localhost:5001/api/v1.0/users/{0}".format(user_id), params=None)
    resData = res.json()
    if resData['Success']:
        return render_template('admin/users/editUser.html', user=resData['data'])
    else:
        return render_template('errors/404.html'), 404

@admin.route('/lives')
@admin_required
def lives():
    return render_template('admin/lives/lives.html')


@admin.route('/lives/create')
@admin_required
def create_live():
    return render_template('admin/lives/createLive.html')

@admin.route('/lives/<int:live_id>/edit')
@admin_required
def edit_live(live_id):
    res = requests.get("http://localhost:5001/api/v1.0/lives/{0}".format(live_id), params=None)
    resData = res.json()
    if resData['Success']:
        return render_template('admin/lives/editLive.html', live=resData['data'])
    else:
        return render_template('errors/404.html'), 404
