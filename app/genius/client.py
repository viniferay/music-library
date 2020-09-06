import os

import requests


TOKEN = 'Bearer ' + os.environ.get('GENIUS_OUTH2')
BASE_URL = 'http://api.genius.com/'


def get_artist_songs(artist_id):
    url = f'{BASE_URL}artists/{artist_id}/songs?sort=popularity&per_page=10'
    response = requests.get(url=url, headers={'Authorization': TOKEN})

    return response


def get_artist_data(artist_id):
    url = f'{BASE_URL}artists/{artist_id}'
    response = requests.get(url=url, headers={'Authorization': TOKEN})

    return response
