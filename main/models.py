from django.db import models


class Recording(models.Model):
    original = models.FileField(upload_to="original/")
    cleaned = models.FileField(upload_to="cleaned/", blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original.name