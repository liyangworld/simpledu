from flask import Blueprint, render_template
import requests


user = Blueprint('user', __name__, url_prefix='/users')

@user.route('/<username>')
def index(username):
    r = requests.get("http://localhost:5001/api/v1.0/users/username/{0}".format(username), params=None)
    resData = r.json()
    if resData['Success']:
        return render_template('users/user.html', user=resData['data'])
    else:
        return render_template('errors/404.html'), 404


