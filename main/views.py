from pathlib import Path

from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render

from .cleaning import clean_audio
from .forms import RecordingForm
from .models import Recording


def home_view(request):
    if request.method == "POST":
        form = RecordingForm(request.POST, request.FILES)
        if form.is_valid():
            recording = form.save()  # original saqlandi

            input_path = Path(recording.original.path)
            output_name = f"{input_path.stem}_cleaned.wav"
            output_path = Path(settings.MEDIA_ROOT) / "cleaned" / output_name
            output_path.parent.mkdir(parents=True, exist_ok=True)

            clean_audio(input_path, output_path)

            recording.cleaned.name = f"cleaned/{output_name}"
            recording.save()
            return redirect("result", pk=recording.pk)
    else:
        form = RecordingForm()
    return render(request, "main/index.html", {"form": form})


def result_view(request, pk):
    recording = get_object_or_404(Recording, pk=pk)
    return render(request, "main/result.html", {"recording": recording})


def recordings_view(request):
    recordings = Recording.objects.order_by("-uploaded_at")
    return render(request, "main/recordings.html", {"recordings": recordings})