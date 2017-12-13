
from flask_restful import Api
from flask_restful.utils import cors
from flask_cors import CORS

from .users import UserItem, UserItemUsername, UserList, Login
from .courses import CourseList, CourseItem
from .lives import LiveList, LiveItem
from .chapters import ChapterItem

def add_resources(app):
    api = Api(app)
    # api.decorators = [cors.crossdomain(origin='*')]

    cors = CORS(app, resources={"/api/*": {"origins": "*"}})

    api.add_resource(Login, '/api/v1.0/login')

    api.add_resource(UserList, '/api/v1.0/users/')
    api.add_resource(UserItem, '/api/v1.0/users/<int:user_id>')
    api.add_resource(UserItemUsername, '/api/v1.0/users/username/<string:username>')

    api.add_resource(CourseList, '/api/v1.0/courses/')
    api.add_resource(CourseItem, '/api/v1.0/courses/<int:course_id>')

    api.add_resource(ChapterItem, '/api/v1.0/courses/<int:course_id>/chapters/<int:chapter_id>')



    api.add_resource(LiveList, '/api/v1.0/lives/')
    api.add_resource(LiveItem, '/api/v1.0/lives/<int:live_id>')


