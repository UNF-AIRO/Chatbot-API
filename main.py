import os
import nltk
from flask import Flask, request
import chatbot as cb
app = Flask(__name__)


@app.route("/")
def hello_world():
    name = os.environ.get("NAME", "World")
    return "Hello {}!".format(name)

@app.route("/test")
def test():
    text = request.args.get('text')
    return {"response": cb.chatbot_response(text)}
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))