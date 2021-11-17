import pickle
import numpy as np
import requests



model = pickle.load(open('NN.pkl', 'rb'))


def pickle_model(song_params):
    song_params = np.array([song_params])
    pred_song = model.predict(song_params)
    return pred_song


feature_columns = ['acousticness', 'danceability', 'duration_ms',
                    'energy', 'instrumentalness', 'liveness',
                    'loudness', 'speechiness', 'tempo','valence']

