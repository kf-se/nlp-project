from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class VideoModel(db.Model):
    __tablename__ = 'video'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)
    comments = db.relationship('CommentsModel', backref='video', lazy=True) 

    def __init__(self, id=None, name=None, views=None, likes=None, comments=None):
        self.id = id
        self.name = name
        self.views = views
        self.likes = likes
        self.comments = comments

    def __repr__(self):
        return f"name={name}, views={views}, likes={likes}"

class CommentsModel(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String(255), nullable=False)
    video_id = db.Column(db.Integer, db.ForeignKey('video.id'), nullable=False)

    def __init__(self, id=None, comment=None, video_id=None):
        self.id = id
        self.comment = comment
        self.video_id = video_id

    def __repr__(self):
        return f"comments={comment}, video_id={video_id}"

db.create_all()

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=str, help="Views of the video is required", required=True)
video_put_args.add_argument("likes", type=str, help="Likes on the video is required", required=True)

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("views", type=str, help="Views of the video")
video_update_args.add_argument("likes", type=str, help="Likes on the video")
video_update_args.add_argument("name", type=str, help="Name of the video")

resource_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'views': fields.Integer,
    'likes': fields.Integer
}

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self, video_id): 
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with that id")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        args = video_put_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            abort(409, message="Video id taken...")

        video = VideoModel(id=video_id, name=args['name'],
                            views=args['views'], likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video does not exist")

        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']
        
        db.session.commit()
        return result

    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Video does not exist")

        db.session.delete(result)
        db.session.commit()
    
        return '', 204

comment_put_args = reqparse.RequestParser()
comment_put_args.add_argument("comment", type=str, help="Comment on the video is required", required=True)

resource_fields_comment = {
    'id': fields.Integer,
    'comment': fields.String
}

class Comment(Resource):
    @marshal_with(resource_fields_comment)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with that id")
        return result

    @marshal_with(resource_fields_comment)
    def put(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with that id")
        pass

    @marshal_with(resource_fields_comment)
    def patch(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with that id")
        pass

    @marshal_with(resource_fields_comment)
    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message="Could not find video with that id")
        pass

api.add_resource(Video, "/video/<string:video_id>")
api.add_resource(Comment, "/video/comment/<string:video_id>")

if __name__== "__main__":
    app.run(debug=True)