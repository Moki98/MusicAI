import audioflux


def extract_pitch_features(audio_data, sr):
    pitch_detect = audioflux.Pitch(
        pitch_type=None,
        samplate=sr,
        low_fre=27.5,
        high_fre=2093.004522404789,
        radix2_exp=12,
        slide_length=1024,
        auto_length=2048,
    )
    pitch_values = pitch_detect.pitch(audio_data)
    return pitch_values
