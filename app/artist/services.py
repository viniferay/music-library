from app.genius.client import get_artist_songs


def get_songs_by_artist_id(artist_id: int) -> dict:
    genius_response = get_artist_songs(artist_id)
    response_json = genius_response.json()['response']

    return response_json
