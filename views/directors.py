from flask_restx import Resource, Namespace
from flask import request

from dao.model.director import DirectorSchema, PaginatedDirectorSchema
from helpers.decorators import admin_required, auth_required
from implemented import director_service

director_ns = Namespace('directors')


@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        rs = director_service.get_all()
        res = PaginatedDirectorSchema().dump(rs)
        return res, 200
    
    @admin_required
    def post(self): 
        req = request.json
        director = director_service.create(req)
        return '', 201


@director_ns.route('/<int:rid>')
class DirectorView(Resource):
    @auth_required
    def get(self, rid):
        r = director_service.get_one(rid)
        sm_d = DirectorSchema().dump(r)
        return sm_d, 200
    
    @admin_required
    def put(self, rid): 
        req = request.json 
        if "id" not in req:
            req["id"] = rid
        director_service.update(req)
        return "", 204

    @admin_required
    def delete(self, rid): 
        director_service.delete(rid)
        return '', 204
