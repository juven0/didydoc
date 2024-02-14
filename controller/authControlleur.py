from flask import request, jsonify
from controller.userController import UsersController
from database.database import get_db


db = get_db()
user = UsersController(db)

class Authentification:
   def __init__(self) -> None:
      pass
    
   def login(email, password):
      # user = user.ged_by_email(email)
      # if user and user['password']== password:
      #    return True
      # else:
      #    return False
      return True
