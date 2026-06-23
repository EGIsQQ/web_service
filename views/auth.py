from flask_restx import Resource, Namespace
from flask import request

from implemented import user_service, auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
class AuthsView(Resource):
    def post(self): 
        user_d = request.json
        user = user_service.create(user_d), 201
        return '', 201
    


@auth_ns.route('/login')
class AuthsView(Resource):
    def post(self): 
        data = request.json

        email = data.get('email', None)
        password = data.get('password', None)


        if None in [email, password]: 
            return '', 401
        
        tokens = auth_service.generate_tokens(email, password)
        return tokens, 201
    
    def put(self): 
        data = request.json
        token = data.get('refresh_token')

        tokens = auth_service.approve_refresh_token(token)

        return tokens, 201

