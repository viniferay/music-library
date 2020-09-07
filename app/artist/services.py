from app import dynamoDB, cache
from app.genius.client import get_artist_songs, get_artist_data


def get_songs_by_artist_id(artist_id: int, caching=True) -> dict:
    if caching is True:
        cache_data = cache.get(str(artist_id))
    else:
        cache_data = None

    if not cache_data:
        artist_data = get_artist_data(artist_id)
        artist_name = artist_data.json()['response']['artist']['name']

        genius_response = get_artist_songs(artist_id)
        response_json = genius_response.json()['response']
        response_json['artist_name'] = artist_name

    else:
        artist_name = cache_data['artist_name']
        response_json = cache_data

    dynamoDB.put_data(artist_name)

    if caching and not cache_data:
        cache.set(str(artist_id), response_json, timeout=168 * 60)

    return response_json
