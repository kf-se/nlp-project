from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class VideoModel(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    comments = db.relationship(
        'CommentModel', 
        backref='video',
        cascade='all, delete, delete-orphan',
        single_parent=True,
        lazy=True
    ) 

    def __init__(self, id=None, name=None, views=None, likes=None):
        self.id = id
        self.name = name
        self.views = views
        self.likes = likes

    def __repr__(self):
        return f"video(name={name}, views={views}, likes={likes}, comments={comments})"

class CommentModel(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1000), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)

    def __init__(self, id=None, content=None, video_id=None):
        self.id = id
        self.content = content
        self.video_id = video_id

    def __repr__(self):
        return f"comment(content={content}, video_id={video_id})"