from flask import Flask
app = Flask(__name__)

@app.route('/<username>')
def get_name(username):
    return username