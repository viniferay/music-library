from marshmallow import Schema, fields


class PrimaryArtistSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    url = fields.URL()
