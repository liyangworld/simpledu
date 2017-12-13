
from flask_restful import Resource, Api, fields, marshal_with, marshal
from webApi2.models import Chapter
from flask import request, current_app


chapter_fields = {
    'id':   fields.Integer,
    'name':   fields.String,
    'description': fields.String,
    'vedio_url': fields.String,
    'vedio_duration': fields.String
}



class ChapterItem(Resource):

    def get(self, course_id, chapter_id):
        chapter = Chapter.query.filter_by(id=chapter_id).first()
        if chapter is None:
            return {'Success': False, 'Message': '章节 {0} 不存在'.format(chapter_id)}

        return {'Success': True, 'Message': '', 'data': marshal(chapter, chapter_fields)}


