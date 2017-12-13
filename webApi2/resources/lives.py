
from flask_restful import Resource, fields, marshal_with, marshal, reqparse
from webApi2.models import db, Live, User
from flask import request, current_app


live_fields = {
    'id':   fields.Integer,
    'name':   fields.String,

    'author_name':   fields.String(attribute=lambda x: x.author.username),
    'author_id':   fields.String(attribute=lambda x: x.author.id)
}

create_live_parser = reqparse.RequestParser()
create_live_parser.add_argument('name', dest='name', type=str, required=True)
create_live_parser.add_argument('author_id', dest='author_id', type=int, required=True)

class LiveList(Resource):

    def get(self):
        pageIndex = request.args.get('pageIndex', default=1, type=int)
        pageSize = request.args.get('pageSize', default=current_app.config['COUNTS_PER_PAGE'], type=int)
        offset = (pageIndex - 1) * pageSize

        query_obj = Live.query
        counts = query_obj.count()
        lives = query_obj.offset(offset).limit(pageSize).all()
        return {'Success': True, 'Message': '', 'data': marshal(lives, live_fields), 'total': counts}

    def post(self):
        datas = create_live_parser.parse_args()

        user = User.query.filter_by(id=datas.author_id).first()
        if not user:
            return {'Success': False, 'Message': '该作者不存在'}

        live = Live()

        live.name = datas.name
        live.author_id = datas.author_id

        db.session.add(live)
        db.session.commit()
        return {'Success': True, 'Message': '', 'live_id': live.id}


class LiveItem(Resource):

    def get(self, live_id):
        live = Live.query.filter_by(id=live_id).first()
        if live is None:
            return {'Success': False, 'Message': '直播 {0} 不存在'.format(live_id)}

        return {'Success': True, 'Message': '', 'data': marshal(live, live_fields)}

    def delete(self, live_id):
        live = Live.query.filter_by(id=live_id).first()
        if live is None:
            return {'Success': False, 'Message': '直播 {0} 不存在'.format(live_id)}
        db.session.delete(live)
        db.session.commit()
        return {'Success': True, 'Message': ''}

    def put(self, live_id):
        datas = create_live_parser.parse_args()

        user = User.query.filter_by(id=datas.author_id).first()
        if not user:
            return {'Success': False, 'Message': '该作者不存在'}

        live = Live.query.filter_by(id=live_id).first()
        if live is None:
            return {'Success': False, 'Message': '直播 {0} 不存在'.format(live_id)}

        live.name = datas.name
        live.author_id = datas.author_id

        db.session.commit()
        return {'Success': True, 'Message': ''}










