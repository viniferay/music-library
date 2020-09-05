from marshmallow import Schema, fields


class PrimaryArtistSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    url = fields.URL()


class SongSchema(Schema):
    id = fields.Integer()
    full_title = fields.String(data_key='fullTitle')
    title = fields.String()
    primary_artist = fields.Nested(PrimaryArtistSchema, data_key='primaryArtist')


class SongsSchema(Schema):
    songs = fields.List(fields.Nested(SongSchema), many=True)
