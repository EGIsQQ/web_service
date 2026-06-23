from flask_restx import Resource, Namespace
from flask import request
from dao.model.users import UserSchema
from helpers.decorators import auth_required
from implemented import user_service

user_ns = Namespace('user')


@user_ns.route('/')
class UsersView(Resource):
    @auth_required
    def get(self):
        token = request.headers.get('Authorization').split(' ')[1]
        user_d = user_service.get_user_info(token)
        res = {
            "name": user_d.name, 
            "surname": user_d.surname,
            "favorite_genre": user_d.favorite_genre
        }
        return res, 200
     
    @auth_required
    def patch(self):
        token = request.headers.get('Authorization').split(' ')[1]
        user_update_data = request.json
        user_service.update(user_update_data, token)
        return '', 201
    
@user_ns.route('/password')
class UsersView(Resource):
    @auth_required  
    def put(self): 
        token = request.headers.get('Authorization').split(' ')[1]
        password_old = request.json['password_1']
        password_new = request.json['password_2']
        user_service.update_password(token, password_old, password_new)
        return '', 201
        
