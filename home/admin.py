from django.contrib import admin
from .models import NewsModel, BlogModel, MediaModal

# Register your models here.
admin.site.register(NewsModel)
admin.site.register(BlogModel)
admin.site.register(MediaModal)