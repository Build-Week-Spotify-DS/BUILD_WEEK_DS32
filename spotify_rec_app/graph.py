import matplotlib.pyplot as plt
import math
import numpy as np
from sklearn.preprocessing import MinMaxScaler


feature_columns = ['acousticness', 'danceability', 'duration_ms',
                   'energy', 'instrumentalness', 'liveness',
                   'loudness', 'speechiness', 'tempo', 'valence']


minmax = MinMaxScaler()

d = np.array([0.519, 0.266, 211.0/60000, 0.396, 0.458,
              0.9, -11.005, 0.5, 93.923, 0.197])
# d[2]/60000
fig = plt.figure(figsize=(12, 8))

# number of categories
N = len(feature_columns)

# create a list with the average of all features
value = list(minmax.fit_transform(d.reshape(-1, 1)))

# repeat first value to close the circle
# the plot is a circle, so we need to "complete the loop"
# and append the start value to the end.

value += value[:1]
# calculate angle for each category
angles = [n/float(N)*2*math.pi for n in range(N)]
angles += angles[:1]

# plot
plt.polar(angles, value)
plt.fill(angles, value, alpha=0.3)

# plt.title('Discovery Weekly Songs Audio Features', size=35)

plt.xticks(angles[:-1], feature_columns, size=15)
plt.yticks(color='grey', size=15)
plt.jsonify()
