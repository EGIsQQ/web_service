from setup_db import db
from marshmallow import Schema, fields

class User(db.Model):
    _tablename_ = 'user'
    id = db.Column(db. Integer, primary_key=True)
    email = db.Column(db.String)
    password = db.Column(db.String)
    name = db.Column(db.String)
    surname = db.Column(db.String)
    favorite_genre = db.Column(db.Integer, db.ForeignKey("genre.id"))
    

class UserSchema(Schema): 
    id = fields.Int()
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    favorite_genre = fields.Int()
    password = fields.Str()
    
    