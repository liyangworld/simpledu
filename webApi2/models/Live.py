
from .TimeBase import TimeBase, db


class Live(TimeBase):
    __tablename__ = 'live'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True, index=True, nullable=False)

    # ondelete='SET NULL'
    author_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    author = db.relationship('User', uselist=False)



