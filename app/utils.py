from app.models import User

from flask import request

def get_user_from_token():
    token = request.headers.get('Authorization')
    if not token:
        return None
    return User.query.filter_by(token=token).first()