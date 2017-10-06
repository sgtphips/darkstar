from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from .models import Audio, Video

# Create your views here.
class AudioListView(ListView):
	context_object_name = 'audio'
	template_name = 'media/audio/audio_list.html'
	model = Audio


class VideoListView(ListView):
	context_object_name = 'video'
	template_name = 'media/video/video_list.html'
	model = Video