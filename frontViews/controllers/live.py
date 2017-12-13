from flask import Blueprint, render_template

live = Blueprint('live', __name__, url_prefix='/lives')

@live.route('/')
def index():
    return render_template('lives/index.html')
