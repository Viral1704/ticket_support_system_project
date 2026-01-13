from flask import Blueprint, request, jsonify

from app import db

from app.models import User

import secrets

auth = Blueprint('auth', __name__)


@auth.route('/login', methods = ['POST'])
def login():
    data = request.get_json() or {}
    email = data.get('email')
    password = data.get('password')
    
    if not email or not password:
        return jsonify({'error': 'Email and password are required'}), 400
    
    user = User.query.filter_by(email=email).first()

    if user is None or not user.check_password(password):
        return jsonify({'message' : 'Invalid email or password'}), 401
    
    token = secrets.token_hex(16)
    user.token = token

    db.session.commit()

    return jsonify({'message': 'Login successful', 'token' : token}), 200


@auth.route('/register', methods = ['POST'])
def register():
    data = request.get_json() or {}
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message' : 'Username, email and password are required'}), 400
    
    user = User.query.filter_by(email = email).first()
    if user is not None:
        return jsonify({'message' : "Email already registered"}), 400
    
    new_user = User(username = username, email = email)
    new_user.password = password

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message' : 'User registered successfully', 
                    'user_id' : new_user.id,
                    }), 201



def get_user_from_token():
    token = request.headers.get('Authorization')
    if not token:
        return None
    return User.query.filter_by(token=token).first()