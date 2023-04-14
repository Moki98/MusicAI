import librosa


def extract_mfcc_features(audio_data, sr):
    mfcc = librosa.feature.mfcc(
        y=audio_data, sr=sr, n_mfcc=13, dct_type=2, norm="ortho", lifter=0
    )
    return mfcc
