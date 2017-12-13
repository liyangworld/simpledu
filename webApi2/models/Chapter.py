
from .TimeBase import TimeBase, db

class Chapter(TimeBase):
    __tablename__ = 'chapter'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True)
    description = db.Column(db.String(256))
    # 课程视频的 url 地址
    vedio_url = db.Column(db.String(256))
    # 视频时长，格式：'30:15'、'1:15:20'
    vedio_duration = db.Column(db.String(24))
    # 关联到课程，并且课程删除及联删除相关章节
    course_id = db.Column(db.Integer, db.ForeignKey('course.id', ondelete="CASCADE"))
    course = db.relationship('Course', uselist=False)

    def __repr__(self):
        return '<Chapter:{}>'.format(self.name)


