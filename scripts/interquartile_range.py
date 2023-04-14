import numpy as np

def remove_outliers(feature_data, feature_keys, multiplier=1.5):
    cleaned_data = []
    for track in feature_data:
        is_outlier = False
        for key in feature_keys:
            q1, q3 = np.percentile(track[key], [25, 75])
            iqr = q3 - q1
            lower_bound = q1 - multiplier * iqr
            upper_bound = q3 + multiplier * iqr

            if np.any((track[key] < lower_bound) | (track[key] > upper_bound)):
                is_outlier = True
                break

        if not is_outlier:
            cleaned_data.append(track)

    return cleaned_data

feature_data_cleaned = remove_outliers(feature_data, feature_keys)
