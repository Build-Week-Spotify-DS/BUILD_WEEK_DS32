import pandas as pd
import pickle


def KNN_pipeline(song_features):
    '''
    Takes in vectorized song features, normalizes data, and uses KNN model to
    predict the 5 songs closest to the given data.
    Requires norm.pkl and NN.pkl to be saved in the same directory.

    Vectorized feature order
    ------------------------
    ['acousticness', 'danceability', 'duration_ms', 'energy',
       'instrumentalness', 'liveness', 'loudness', 'speechiness', 'tempo',
       'valence']
    '''

    # Read in required .csv file
    df = pd.read_csv('25ksongs.csv', index_col=0)

    # Load models
    norm = pickle.load(open('norm.pkl', 'rb'))
    knn = pickle.load(open('NN.pkl', 'rb'))

    # Normalize features
    normed = norm.transform([song_features])

    # Find five nearest neighbors, returns df indices
    nn_5 = knn.kneighbors(normed, 5, return_distance=False)

    # Gather urls from df for the five nearest neighbors
    urls = df.loc[nn_5[0]]['url']
    # Format them to list
    links = urls.tolist()

    # return nn_5
    return links, normed
