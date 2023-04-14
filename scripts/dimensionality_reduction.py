import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Load the feature data
feature_data = np.load('../data/feature_data.npy', allow_pickle=True)

# Combine all the features into a single matrix (X)
feature_keys = ['chroma', 'tonnetz', 'mfcc', 'zcr', 'onset_strength_envelope', 'tempo', 'pitch_values', 'local loudness']
X = []
for track in feature_data:
    track_features = []
    for key in feature_keys:
        if key == 'pitch_values':
            track_features.extend(track[key][0])
            track_features.extend(track[key][1])
            track_features.extend(track[key][2])
        elif key == 'local loudness':
            track_features.extend(track[key].flatten())
        else:
            track_features.extend(track[key].flatten())
    X.append(track_features)

X = np.array(X)

# Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Perform PCA
pca = PCA(n_components=2)  # Change n_components to the desired number of reduced dimensions
X_pca = pca.fit_transform(X_scaled)

# Save the reduced data
np.save('../data/reduced_data.npy', X_pca)
