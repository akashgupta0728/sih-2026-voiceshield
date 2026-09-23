import numpy as np
import librosa

TARGET_SR = 16000

def bytes_to_array(data: bytes) -> np.ndarray:
    # assumes incoming audio is 16-bit PCM
    audio = np.frombuffer(data, dtype=np.int16).astype(np.float32) / 32768.0
    return audio

def resample(audio: np.ndarray, orig_sr: int) -> np.ndarray:
    if orig_sr == TARGET_SR:
        return audio
    return librosa.resample(audio, orig_sr=orig_sr, target_sr=TARGET_SR)

def is_speech(audio: np.ndarray, threshold: float = 0.01) -> bool:
    # placeholder VAD — energy-based, swap for webrtcvad/silero later
    rms = np.sqrt(np.mean(audio**2))
    return rms > threshold