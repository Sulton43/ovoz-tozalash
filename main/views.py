import io
import librosa
import noisereduce as nr
import soundfile as sf
from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    # 1. Agar foydalanuvchi "Tozalash" tugmasini bosib, fayl yuborgan bo'lsa (POST so'rov):
    if request.method == 'POST' and request.FILES.get('audio_file'):
        uploaded_file = request.FILES['audio_file']
        
        # 2. Yuklangan audioni librosa orqali o'qib olamiz
        data, rate = librosa.load(uploaded_file, sr=None)
        
        # 3. Shovqinni tozalaymiz (prop_decrease=0.8 shovqinni 80% ga pasaytiradi)
        reduced_noise = nr.reduce_noise(y=data, sr=rate, prop_decrease=0.8)
        
        # 4. Tozalangan ovozni kompyuter xotirasiga (buferga) WAV formatda yozamiz
        buffer = io.BytesIO()
        sf.write(buffer, reduced_noise, rate, format='WAV')
        buffer.seek(0)
        
        # 5. Tayyor faylni brauzerga yuklab olish uchun qaytarib beramiz
        response = HttpResponse(buffer.read(), content_type='audio/wav')
        response['Content-Disposition'] = f'attachment; filename="tozalangan_{uploaded_file.name}.wav"'
        return response

    # Agar foydalanuvchi sahifaga shunchaki kirgan bo'lsa (GET so'rov), formani ko'rsatamiz:
    return render(request, 'main/index.html')   