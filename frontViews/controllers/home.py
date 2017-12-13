from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_user, logout_user, login_required

import requests
import json
from frontViews.models import User


# 省略了 url_prifix，那么默认就是 '/'
home = Blueprint('home', __name__)

@home.route('/')
def index():
    return redirect(url_for('course.index'))

@home.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('home/login.html')
    if request.method == 'POST':
        # 验证提交的数据
        pre_data = request.get_json()
        email = pre_data['email']
        password = pre_data['password']
        remember_me = pre_data['remember_me']

        payload = {
            "email": email,
            "password": password
        }
        r = requests.post("http://localhost:5001/api/v1.0/login", json=payload)
        resData = r.json()

        if not resData['Success']:
            return jsonify({"Success": False, "Message": resData['Message']})
        user_data = resData['data']
        user = User()
        user.id = user_data['id']
        user.username = user_data['username']
        user.email = user_data['email']
        user.role = user_data['role']

        login_user(user, remember=remember_me)
        return jsonify({"Success": True, "Message": ''})

@home.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))


@home.route('/register')
def register():
    return render_template('home/register.html')
