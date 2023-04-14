import librosa


def extract_temporal_features(audio_data, sr):
    onset_env = librosa.onset.onset_strength(y=audio_data, sr=sr)
    tempo = librosa.beat.tempo(y=None, sr=sr, onset_envelope=onset_env)
    return onset_env, tempo
