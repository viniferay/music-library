from flask import jsonify, request

from app.artist import bp
from app.artist.schemas import SongsSchema
from app.artist.services import get_songs_by_artist_id


@bp.route('/artists/<int:artist_id>/songs', methods=['GET'])
def get_songs_from_artist(artist_id):
    schema = SongsSchema()

    caching = request.args.get('cache', True)
    songs = get_songs_by_artist_id(artist_id, caching)

    return jsonify(schema.dump(songs)), 200
