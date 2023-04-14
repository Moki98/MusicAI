"""Extracts chroma features from audio data."""
import librosa


def extract_chroma_features(audio_data, sr):
    '''Extracts chroma features from audio data.
    '''
    chroma = librosa.feature.chroma_stft(
        y=audio_data, sr=sr, n_fft=2048, hop_length=512, win_length=None,
        window='hann', center=True, pad_mode='constant', tuning=None, n_chroma=12
    )
    return chroma
