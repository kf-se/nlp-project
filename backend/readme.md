# Flask
Build an endpoint that serves a response, i.e. *make_response()*

Determine where virtualenv is:
pip -V

To start:
- Execute main.py file

Creating REST-api with flask:
https://youtu.be/GMppyAPbLYk?t=1671

**Example requests**
http://127.0.0.1:5000/video/<string:video_id>

PUT: curl -X PUT -H "Content-Type: application/json" --data '{"name": "tim", "views": "20", "likes": "20"}' http://127.0.0.1:5000/video/21

GET: curl -X GET http://127.0.0.1:5000/video/20

DELETE: curl -X DELETE http://127.0.0.1:5000/video/20
