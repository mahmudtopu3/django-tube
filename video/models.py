import os
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.text import slugify

def validate_mp4_extension(value):
    ext = os.path.splitext(value.name)[1]  # Get the file extension
    if ext.lower() != '.mp4':
        raise ValidationError("Only .mp4 files are allowed.")


class Video(models.Model):
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    COMPLETED = 'Completed'
    
    STATUS_CHOICES = (
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (COMPLETED, 'Completed'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, blank=True)
    description = models.TextField()
    video = models.FileField(upload_to="videos",validators=[validate_mp4_extension])
    thumbnail = models.ImageField(upload_to="thumbnails",null=True,blank=True)
    duration = models.CharField(max_length=20, blank=True,null=True)
    hls = models.CharField(max_length=500,blank=True,null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    is_running = models.BooleanField(default=False)
  
    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)