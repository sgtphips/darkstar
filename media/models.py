from django.db import models
from django.utils import timezone
# Create your models here.
class Audio(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	link_to_audio = models.CharField(max_length=200)
	description = models.TextField()
	featured_image = models.URLField(max_length=500)
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	# This removes the extra 's' in the admin panel
	# Instead of it saying 'Medias' it will say 'Media'
	class Meta:
		verbose_name_plural = "Audio"


class Video(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	embed_code = models.CharField(max_length=500)
	description = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

	# This removes the extra 's' in the admin panel
	# Instead of it saying 'Medias' it will say 'Media'
	class Meta:
		verbose_name_plural = "Video"