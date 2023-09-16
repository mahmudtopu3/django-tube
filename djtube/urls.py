"""
URL configuration for djtube project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from video.views import hls_video_player, serve_hls_playlist,serve_hls_segment
urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/<int:video_id>/', hls_video_player, name='hls_video_player'),
    path('serve_hls_playlist/<int:video_id>/', serve_hls_playlist, name='serve_hls_playlist'),
    path('serve_hls_segment/<int:video_id>/<str:segment_name>/',serve_hls_segment, name='serve_hls_segment'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)