import pickle


def pkl_model():
    open_pick = open('NN.pkl', 'rb')
    model = pickle.load(open_pick)

    song = scaler.fit_transform(get_song_params(track_id))
    model = model.kneighbors(song, 5, return_distance=False)
    return model
