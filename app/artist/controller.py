from flask import jsonify

from app.artist import bp
from app.artist.schemas import SongsSchema
from app.artist.services import get_songs_by_artist_id


@bp.route('/artists/<int:artist_id>/songs', methods=['GET'])
def get_songs_from_artist(artist_id):
    schema = SongsSchema()
    songs = get_songs_by_artist_id(artist_id)

    return jsonify(schema.dump(songs)), 200
