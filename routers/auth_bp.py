from flask import Blueprint
from controller.user_controller import signup, login

auth_bp = Blueprint("auth", __name__, "/auth")

# Signup route
@auth_bp.route("/signup", method=['POST'])
def handlerSignup ():
    return signup()

# Login route
@auth_bp.route("/login", method=['POST'])
def handlerLogin():
    return login()
