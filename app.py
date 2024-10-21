from flask import Flask
from routers import auth_bp, cart_bp, product_bp
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Setting up a database
db = SQLAlchemy(app)

#routes available
@app.route("/", methods=["Get"])
def welcome ():
    return "Welcome to BeShopy"


#routes in BeShopy (blueprints)
@app.register_blueprint(auth_bp)
@app.register_blueprint(product_bp)
@app.register_blueprint(cart_bp)


