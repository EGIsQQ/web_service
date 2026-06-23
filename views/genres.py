from flask_restx import Resource, Namespace
from flask import request

from dao.model.genre import GenreSchema, PaginatedGenreSchema
from helpers.decorators import admin_required, auth_required
from implemented import genre_service

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    # @auth_required
    def get(self):
        rs = genre_service.get_all()
        res = PaginatedGenreSchema().dump(rs)
        return res, 200
    
    @admin_required
    def post(self): 
        req = request.json
        genre = genre_service.create(req)
        return '', 201


@genre_ns.route('/<int:rid>')
class GenreView(Resource):
    @auth_required
    def get(self, rid):
        r = genre_service.get_one(rid)
        sm_d = GenreSchema().dump(r)
        return sm_d, 200
    
    @admin_required
    def put(self, rid): 
        req = request.json
        if 'id' not in req: 
            req['id'] = rid
        genre_service.update(req)
        return '', 204
    
    @admin_required
    def delete(self, rid): 
        genre_service.delete(rid)
        return '', 204