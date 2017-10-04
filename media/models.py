from django.db import models
from django.utils import timezone
# Create your models here.
class Media(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	featured_img = models.FileField(upload_to='uploads/')
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.exp_title