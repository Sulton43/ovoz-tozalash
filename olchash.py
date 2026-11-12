import glob
import numpy as np
import librosa

ASL = "media/original/England.wav"  # asl faylingiz


def fon_va_nutq_farqi(path):
    data, rate = librosa.load(path, sr=None)
    kadr = rate // 2  # yarim soniyalik bo'laklar
    darajalar = []
    for i in range(0, len(data) - kadr, kadr):
        bolak = data[i:i + kadr]
        rms = np.sqrt(np.mean(bolak ** 2)) + 1e-10
        darajalar.append(20 * np.log10(rms))
    fon = np.percentile(darajalar, 5)     # eng jim bo'laklar (faqat shovqin)
    nutq = np.percentile(darajalar, 90)   # eng baland bo'laklar (gap)
    return nutq - fon


print("ASL:", round(fon_va_nutq_farqi(ASL), 1), "dB")
for f in sorted(glob.glob("variantlar/*.wav")):
    print(f, round(fon_va_nutq_farqi(f), 1), "dB")