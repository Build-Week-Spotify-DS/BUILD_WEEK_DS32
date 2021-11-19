import requests
import pandas as pd
import numpy as np
from os import getenv
feature_columns = ['acousticness', 'danceability', 'duration_ms',
                   'energy', 'instrumentalness', 'liveness',
                   'loudness', 'speechiness', 'tempo', 'valence']


def get_song_params(song_link):

    CLIENT_ID = getenv('CLIENT_ID')
    CLIENT_SECRET = getenv('CLIENT_SECRET')
    AUTH_URL = 'https://accounts.spotify.com/api/token'

    auth_response = requests.post(AUTH_URL, {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })

    auth_response_data = auth_response.json()

    access_token = auth_response_data['access_token']
    auth_response_data

    headers = {'Authorization': f'Bearer {access_token}'}

    track_id = song_link.split('/')[-1].split('?')[0]
    r = requests.get(
        'https://api.spotify.com/v1/audio-features/'+track_id, headers=headers)
    r.json()

    df = pd.DataFrame([r.json()])
    df['duration_ms'] = df['duration_ms']/60000
    song_param = np.array(df[feature_columns])[0].reshape(-1, 1)
    np.set_printoptions(suppress=True)
    return df[feature_columns].columns, song_param
