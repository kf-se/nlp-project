from flask import Flask, make_response

app = Flask(__name__)

@app.route("/api/v2/test_response")
def test_response():
    headers = {"Content-Type": "application/json"}
    return make_response(
        'Test worked!',
        200,
        header=headers
    )

@app.get("/hello")
def hello():
    return "Hello world!"

if __name__== "__main__":
    app.run(port=4000)