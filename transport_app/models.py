from django.db import models

class Transport(models.Model):
	source = models.CharField(max_length=200)
	destination = models.CharField(max_length=200)
	amount = models.CharField(max_length=200)

	def __str__(self):
		return self.source
