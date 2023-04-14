"""Extract features for all mp3 files in the data/tracks directory and save
them in batches of 100.
"""

import os
import numpy as np
from tqdm import tqdm
from extract_features import extract_features_for_files


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


if __name__ == "__main__":
    data_path = "../data/tracks"
    batch_size = 100
    mp3_files = [file for file in os.listdir(data_path) if file.endswith(".mp3")]
    total_batches = len(mp3_files) // batch_size + 1

    for batch_num, batch_files in tqdm(
        enumerate(chunks(mp3_files, batch_size)),
        total=total_batches,
        desc="Processing batches",
    ):
        feature_data = extract_features_for_files(batch_files, data_path)
        np.save(f"../data/feature_data_batch_{batch_num}.npy", feature_data)
