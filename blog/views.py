from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from .models import Post

# Create your views here.
class PostListView(ListView):
	context_object_name = 'post'
	template_name = 'blog/post_list.html'
	model = Post