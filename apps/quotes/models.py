from __future__ import unicode_literals

from django.db import models
from ..formv.models import User

# Create your models here.
class Quote(models.Model):
	postedby = models.ForeignKey(User)
	quotedby = models.CharField(max_length= 100)
	message = models.CharField(max_length=140)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

class Favorite(models.Model):
	favoritequote = models.ForeignKey(Quote)
	favoritedby = models.ForeignKey(User)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
