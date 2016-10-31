from __future__ import unicode_literals

from django.db import models
from ..formv.models import User

# Create your models here.
class QuoteManager(models.Manager):
	def validate_post(self, post):
		errors = []
		if len(post['quotedby']) == 0:
			errors.append("Quoted by is required")
		elif len(post['quotedby']) < 3:
			errors.append("Quoted by must be at least 3 characters")

		if len(post['message']) == 0:
			errors.append("Message is required")
		elif len(post['message']) < 10:
			errors.append("Message must be at least 10 characters")
		return errors

class Quote(models.Model):
	postedby = models.ForeignKey(User)
	quotedby = models.CharField(max_length= 100)
	message = models.CharField(max_length=140)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = QuoteManager()

class Favorite(models.Model):
	favoritequote = models.ForeignKey(Quote)
	favoritedby = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
