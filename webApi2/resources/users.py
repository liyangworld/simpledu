
from flask_restful import Resource, Api, fields, marshal_with, marshal, reqparse
from webApi2.models import db, User
from werkzeug.security import generate_password_hash, check_password_hash
from flask import request, current_app

course_fields = {
    'name':   fields.String
}
user_fields = {
    'id': fields.Integer,
    'username': fields.String,
    'email': fields.String,
    'role': fields.Integer,
    'publish_courses': fields.List(fields.Nested(course_fields))
}

Login_post_parser = reqparse.RequestParser()
Login_post_parser.add_argument('email', dest='email', type=str, required=True)
Login_post_parser.add_argument('password', dest='password', type=str, required=True)

class Login(Resource):
    def post(self):
        args = Login_post_parser.parse_args()

        user = User.query.filter_by(email=args.email).first()
        # print(args.email, user)
        if not user:
            return {'Success': False, 'Message': '此邮箱不存在'}
        if not user.check_password(args.password):
            return {'Success': False, 'Message': '密码错误'}
        return {'Success': True, 'Message': '', 'data': marshal(user, user_fields)}


put_user_parser = reqparse.RequestParser()
put_user_parser.add_argument('username', dest='username', type=str, required=True)
put_user_parser.add_argument('email', dest='email', type=str, required=True)

class UserItem(Resource):

    def get(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return {'Success': False, 'Message': '用户 {0} 不存在'.format(user_id)}

        return {'Success': True, 'Message': '', 'data': marshal(user, user_fields)}

    def put(self, user_id):
        datas = put_user_parser.parse_args()

        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return {'Success': False, 'Message': '用户 {0} 不存在'.format(user_id)}

        user.username = datas.username
        user.email = datas.email

        db.session.commit()
        return {'Success': True, 'Message': ''}

    def delete(self, user_id):
        user = User.query.filter_by(id=user_id).first()
        if user is None:
            return {'Success': False, 'Message': '用户 {0} 不存在'.format(user_id)}
        db.session.delete(user)
        db.session.commit()
        return {'Success': True, 'Message': ''}

class UserItemUsername(Resource):

    def get(self, username):
        user = User.query.filter_by(username=username).first()
        if user is None:
            return {'Success': False, 'Message': '用户 {0} 不存在'.format(username)}

        return {'Success': True, 'Message': '', 'data': marshal(user, user_fields)}



UserList_post_parser = reqparse.RequestParser()
UserList_post_parser.add_argument('username', dest='username', type=str, required=True)
UserList_post_parser.add_argument('email', dest='email', type=str, required=True)
UserList_post_parser.add_argument('password', dest='password', type=str, required=True)

def exist_username(name):
    if User.query.filter_by(username=name).first():
        return True
    return False


def exist_email(email):
    if User.query.filter_by(email=email).first():
        return True
    return False

class UserList(Resource):

    def get(self):
        pageIndex = request.args.get('pageIndex', default=1, type=int)
        pageSize = request.args.get('pageSize', default=current_app.config['COUNTS_PER_PAGE'], type=int)
        offset = (pageIndex - 1) * pageSize

        query_obj = User.query
        counts = query_obj.count()
        users = query_obj.offset(offset).limit(pageSize).all()
        return {'Success': True, 'Message': '', 'data': marshal(users, user_fields), 'total': counts}


    def post(self):

        args = UserList_post_parser.parse_args()

        if exist_username(args.username):
            return {'Success': False, 'Message': '用户名已存在'}
        if exist_email(args.email):
            return {'Success': False, 'Message': '邮箱已存在'}

        user = User()
        user.username = args.username
        user.email = args.email
        user.password = args.password

        db.session.add(user)
        db.session.commit()

        return {'Success': True, 'Message': '', 'data': marshal(user, user_fields)}





