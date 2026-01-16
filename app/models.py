from app import db

from werkzeug.security import generate_password_hash, check_password_hash

from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), nullable = False)
    email = db.Column(db.String(120), unique =True, nullable = False)
    password_hash = db.Column(db.String(120), nullable =False)
    token = db.Column(db.String(120), nullable = True)

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(120), nullable = False)
    description = db.Column(db.Text, nullable = True)
    status = db.Column(db.String(20), nullable = False, default = 'open')
    category = db.Column(db.String(20), nullable = False, default = 'general')
    priority = db.Column(db.String(20), nullable = False, default = 'low')
    created_at = db.Column(db.DateTime, default = datetime.utcnow, nullable = False)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow, onupdate = datetime.utcnow, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)