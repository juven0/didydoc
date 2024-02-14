from flask import Blueprint, render_template, jsonify, send_file, request, redirect
from database.database import get_db
from controller.userController import UsersController
from controller.authControlleur import Authentification

user_view = Blueprint('user_routes', __name__, template_folder='/templates')

db = get_db()
userController = UsersController(db)
auth = Authentification()

@user_view.route('/user/login/', methods= ['POST'])
def login():
    data = request.form
    email = data.get('email')
    password = data.get('password')
    return redirect('/books/')
    # if auth.login(email, password):
    #     redirect('/books/')
    # else:
    #     return render_template('login.html')

@user_view.route('/user/login/', methods= ['GET'])
def homelog():
    return render_template('login.html')

@user_view.route('/user/signup/',methods = ['GET'])
def signup():
    return render_template('signup.html')

@user_view.route('/user/signup/',methods = ['POST'])
def signupcreat():
    data = request.form
    email = data.get('email')
    name = data.get('username')
    password = data.get('password')
    userController.create(name, email, password)
    return render_template('login.html')