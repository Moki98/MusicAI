import librosa


def extract_zero_crossing_rate(audio_data, sr):
    zcr = librosa.feature.zero_crossing_rate(
        y=audio_data, frame_length=2048, hop_length=512, center=True
    )
    return zcr
