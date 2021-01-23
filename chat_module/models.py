from django.db import models

# Create your models here.

class message(models.Model):
	message_id = models.IntegerField(primary_key=True)
	user = models.CharField(max_length=50)
	message = models.CharField(max_length=500)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user
