from marshmallow import Schema, fields

from setup_db import db


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


class GenreSchema(Schema):
    id = fields.Int()
    name = fields.Str()

class PaginationSchema(Schema):
    page = fields.Int()
    per_page = fields.Int()
    total = fields.Int()
    pages = fields.Int()
    has_next = fields.Bool()
    has_prev = fields.Bool()

class PaginatedGenreSchema(Schema):
    pagination = fields.Nested(PaginationSchema, allow_none=True)
    items = fields.List(fields.Nested(GenreSchema))