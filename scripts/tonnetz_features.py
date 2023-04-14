import librosa


def extract_tonnetz_features(audio_data, sr):
    chroma = librosa.feature.chroma_cqt(y=audio_data, sr=sr)
    tonnetz = librosa.feature.tonnetz(y=audio_data, sr=sr, chroma=chroma)
    return tonnetz
