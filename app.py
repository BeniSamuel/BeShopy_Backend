from flask import Flask

app = Flask(__name__)

#routes available
@app.route("/", methods=["Get"])
def welcome ():
    return "Welcome to BeShopy"


#routes in BeShopy



