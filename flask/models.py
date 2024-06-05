
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import  Column, Integer, Text, TIMESTAMP
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column('password', db.Text, nullable=False)
    emails   = db.relationship('Email', backref='user', cascade="all, delete-orphan",lazy=True)

    @property
    def password(self):
        raise AttributeError("Password is not a readable attribute")

    @password.setter
    def password(self, plain_text_password):
        self._password = generate_password_hash(plain_text_password)

    def check_password(self, plain_text_password):
        return check_password_hash(self._password, plain_text_password)

class Email(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    email   = db.Column(db.String(120), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',ondelete='CASCADE'),  nullable=False)

