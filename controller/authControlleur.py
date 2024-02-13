from flask import request, jsonify
import userController

class Authentification:
   def __init__(self) -> None:
      pass
    
   def login():
      auth = request.json

      user = userController.ged_by_username(auth['username'])
      if user and user['password']== auth['password']:
         pass
      
      return jsonify({'message': 'Invalid credentials'}), 401
