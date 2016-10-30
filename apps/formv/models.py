from __future__ import unicode_literals
from django.db import models
import bcrypt
import re
import datetime
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



#TODO
# store emails lowercase

class UserManager(models.Manager):
	def login(self, postData):
		user_list = User.objects.filter(email=postData['email']) 

		if user_list:
			user = user_list[0]
			#then check their password
			if bcrypt.hashpw(postData['password'].encode(), user.password.encode()) == user.password:
				#login is valid
				return user
		return None

	def register(self, postData):
		encrypted_password =  bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
		birthday = datetime.datetime.strptime(postData['birthday'], "%Y-%m-%d")
		User.objects.create(name=postData['name'],alias=postData['alias'], email=postData['email'], birthday=birthday,password=encrypted_password)

	def validate_user_info(self, postData):
		errors = []
		if len(postData['name']) == 0:
			errors.append("Name is required")
		elif len(postData['name']) < 3:
			errors.append("Name must be at least 3 characters")
		elif not postData['name'].replace(" ","").isalpha():
			errors.append("Name must only have letters")

		if len(postData['alias']) == 0:
			errors.append("Alias is required")
		elif len(postData['alias']) < 3:
			errors.append("Alias must be at least 3 characters")

		if len(postData['email']) == 0:
			errors.append("Email is required")
		elif not EMAIL_REGEX.match(postData['email']):
			errors.append("Please enter a valid email")

		if len(postData['password']) == 0:
			errors.append('Password is required')
		elif len(postData['password']) < 8:
			errors.append('Password must be at least 8 characters long')
		elif postData['password'] != postData['passconf']:
			errors.append('Passwords must match')

		if len(User.objects.filter(email=postData['email'])) > 0:
			errors.append("Email address is unavailable")
		return errors



# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=45)
	alias = models.CharField(max_length=45)
	email = models.EmailField(max_length=250)
	birthday = models.DateField(null=True)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()




