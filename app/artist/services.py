from app import dynamoDB
from app.genius.client import get_artist_songs, get_artist_data


def get_songs_by_artist_id(artist_id: int) -> dict:
    artist_data = get_artist_data(artist_id)
    artist_name = artist_data.json()['response']['artist']['name']
    dynamoDB.put_data(artist_name)

    genius_response = get_artist_songs(artist_id)
    response_json = genius_response.json()['response']
    response_json['artist_name'] = artist_name

    return response_json
