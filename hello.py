from flask import Flask

app=Flask(__name__)

@app.route("/")
def arthur():
    return 'Hello, Arthur\nGo to <a href"https://tiide3.herokuapp.com/tiide">TIIDE</a>'

@app.route("/tiide")
def tiide():
    return "Welcome to TIIDE World!"
