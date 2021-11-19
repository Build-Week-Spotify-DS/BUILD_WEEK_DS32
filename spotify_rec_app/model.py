import pandas as pd
import pickle


def KNN_pipeline(song_features):

    # Read in required .csv file
    df = pd.read_csv('25ksongs.csv', index_col=0)

    # Load models
    norm = pickle.load(open('norm.pkl', 'rb'))
    knn = pickle.load(open('NN.pkl', 'rb'))

    # Normalize features
    normed = norm.fit_transform(song_features)

    # Find five nearest neighbors, returns df indices
    nn_5 = knn.kneighbors(normed.reshape(1, -1),
                          5, return_distance=False)

    # Gather urls from df for the five nearest neighbors
    urls = df.loc[nn_5[0]]['url'].tolist()
    artist = df.loc[nn_5[0]]['artist_name'].tolist()
    track = df.loc[nn_5[0]]['track_name'].tolist()

    # return nn_5
    return urls, artist, track
