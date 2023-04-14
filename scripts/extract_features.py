"""
This script extracts features from the audio files and saves them to a file
for further processing
"""

import os
import librosa
import numpy as np
from tqdm import tqdm
from chroma_features import extract_chroma_features
from tonnetz_features import extract_tonnetz_features
from mfcc_features import extract_mfcc_features
from zero_crossing_rate import extract_zero_crossing_rate
from temporal_features import extract_temporal_features
from pitch_features import extract_pitch_features
from rms_features import extract_rms_features

data_path = "../data/tracks"
mp3_files = [file for file in os.listdir(data_path) if file.endswith(".mp3")]


def extract_features_for_files(mp3_files, data_path):
    """the function to extract features for all the mp3 files in the data_path

    :param mp3_files: mp3 files to extract features for
    :type mp3_files: list
    :param data_path: path to the data
    :type data_path: str
    :return: list of dictionaries containing the extracted features
    :rtype: list
    """
    feature_data = []
    for file in tqdm(mp3_files, desc="Processing MP3 files"):
        file_path = os.path.join(data_path, file)
        audio_data, sr = librosa.load(file_path, mono=False)
        chroma = extract_chroma_features(audio_data, sr)
        tonnetz = extract_tonnetz_features(audio_data, sr)
        mfcc = extract_mfcc_features(audio_data, sr)
        zcr = extract_zero_crossing_rate(audio_data, sr)
        onset_env, tempo = extract_temporal_features(audio_data, sr)
        pitch_values = extract_pitch_features(audio_data, sr)
        rms = extract_rms_features(audio_data, sr)

        feature_data.append(
            {
                "file": file,
                "chroma": chroma,
                "tonnetz": tonnetz,
                "mfcc": mfcc,
                "zcr": zcr,
                "onset_strength_envelope": onset_env,
                "tempo": tempo,
                "pitch_values": pitch_values,
                "local loudness": rms,
            }
        )

    return feature_data


# Call the function and save the extracted feature data to a file for further processing


feature_data = extract_features_for_files(mp3_files, data_path)
np.save("../data/feature_data.npy", feature_data)
