
from flask_restful import Resource, fields, marshal_with, marshal, reqparse
from webApi2.models import db, Course, User
from flask import request, current_app


chapter_fields = {
    'id':   fields.Integer,
    'name':   fields.String,
    'description': fields.String,
    'vedio_url': fields.String,
    'vedio_duration': fields.String
}

course_fields = {
    'id':   fields.Integer,
    'name':   fields.String,
    'description': fields.String,
    'image_url': fields.String,

    'authorName':   fields.String(attribute=lambda x: x.author.username),
    'authorId':   fields.String(attribute=lambda x: x.author.id),
    'authorJob':   fields.String(attribute=lambda x: x.author.job),
    'chapters':   fields.List(fields.Nested(chapter_fields)),
}
resource_fields = {
    'data': fields.List(fields.Nested(course_fields)),
    'Success': fields.String(default=True),
    'Message': fields.String(default='')
}

create_course_fields = {
    'name':   fields.String,
    'description': fields.String,
    'image_url': fields.String,

    'author_id':   fields.Integer,
}

create_course_parser = reqparse.RequestParser()
create_course_parser.add_argument('name', dest='name', type=str, required=True)
create_course_parser.add_argument('description', dest='description', type=str, required=True)
create_course_parser.add_argument('image_url', dest='image_url', type=str, required=True)
create_course_parser.add_argument('author_id', dest='author_id', type=int, required=True)

class CourseList(Resource):

    def get(self):
        pageIndex = request.args.get('pageIndex', default=1, type=int)
        pageSize = request.args.get('pageSize', default=current_app.config['COUNTS_PER_PAGE'], type=int)
        offset = (pageIndex - 1) * pageSize

        query_obj = Course.query
        counts = query_obj.count()
        courses = query_obj.offset(offset).limit(pageSize).all()
        return {'Success': True, 'Message': '', 'data': marshal(courses, course_fields), 'total': counts}

    def post(self):
        datas = create_course_parser.parse_args()

        user = User.query.filter_by(id=datas.author_id).first()
        if not user:
            return {'Success': False, 'Message': '该作者不存在'}

        course = Course()

        course.name = datas.name
        course.description = datas.description
        course.image_url = datas.image_url
        course.author_id = datas.author_id

        db.session.add(course)
        db.session.commit()
        return {'Success': True, 'Message': '', 'course_id': course.id}



class CourseItem(Resource):

    def get(self, course_id):
        course = Course.query.filter_by(id=course_id).first()
        if course is None:
            return {'Success': False, 'Message': '课程 {0} 不存在'.format(course_id)}

        return {'Success': True, 'Message': '', 'data': marshal(course, course_fields)}

    def delete(self, course_id):
        course = Course.query.filter_by(id=course_id).first()
        if course is None:
            return {'Success': False, 'Message': '课程 {0} 不存在'.format(course_id)}
        db.session.delete(course)
        db.session.commit()
        return {'Success': True, 'Message': ''}

    def put(self, course_id):
        datas = create_course_parser.parse_args()

        user = User.query.filter_by(id=datas.author_id).first()
        if not user:
            return {'Success': False, 'Message': '该作者不存在'}

        course = Course.query.filter_by(id=course_id).first()
        if course is None:
            return {'Success': False, 'Message': '课程 {0} 不存在'.format(course_id)}

        course.name = datas.name
        course.description = datas.description
        course.image_url = datas.image_url
        course.author_id = datas.author_id

        db.session.commit()
        return {'Success': True, 'Message': ''}


