import librosa
import noisereduce as nr
import soundfile as sf


def clean_audio(input_path, output_path, strength=0.8):
    """Audio faylni o'qib, doimiy fon shovqinini tozalaydi va WAV qilib saqlaydi."""
    data, rate = librosa.load(input_path, sr=None)
    reduced = nr.reduce_noise(
        y=data,
        sr=rate,
        stationary=True,      # telefon "fishsh"i doimiy shovqin
        prop_decrease=strength,
        n_fft=2048,           # ovozni tabiiyroq saqlaydi
    )
    reduced = librosa.util.normalize(reduced)  # pasayib qolgan balandlikni tuzatadi
    sf.write(output_path, reduced, rate)