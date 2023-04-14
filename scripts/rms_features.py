import librosa


def extract_rms_features(y, sr):
    rms = librosa.feature.rms(y=y, S=sr)
    return rms
