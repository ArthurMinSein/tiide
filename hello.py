from flask import Flask

app=Flask(__name__)

@app.route("/")
def arthur():
    return "Hello, Arthur"

@app.route("/tiide")
def tiide():
    return "Welcome to TIIDE World!"
