from django.contrib import admin
from .models import Video


class VideoAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Video._meta.get_fields()]

admin.site.register(Video,VideoAdmin)
