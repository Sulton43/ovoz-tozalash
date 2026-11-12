import os
import librosa
import noisereduce as nr
import soundfile as sf

INPUT = "media/original/England.wav"
os.makedirs("variantlar", exist_ok=True)

data, rate = librosa.load(INPUT, sr=None)

variantlar = {
    "A_hozirgi": dict(stationary=False, prop_decrease=0.8),
    "B_stationary": dict(stationary=True, prop_decrease=0.8),
    "C_stationary_nfft2048": dict(stationary=True, prop_decrease=0.8, n_fft=2048),
    "D_yumshoq": dict(stationary=True, prop_decrease=0.6, n_fft=2048),
    "E_silliq": dict(stationary=True, prop_decrease=0.8, n_fft=2048, time_mask_smooth_ms=128),
}

for nom, params in variantlar.items():
    reduced = nr.reduce_noise(y=data, sr=rate, **params)
    reduced = librosa.util.normalize(reduced)
    sf.write(f"variantlar/{nom}.wav", reduced, rate)
    print(nom, "tayyor")