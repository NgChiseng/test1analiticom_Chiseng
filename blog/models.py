from django.db import models
from django.utils import timezone
# Used for import the Django Users of contrib.auth.models
from django.contrib.auth.models import User

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	published_date = models.DateTimeField(blank=True, null=True)

	# Function that save the publish date of a post.
	#
	# @date [06/04/2017]
	#
	# @author [Chiseng Ng]
	#
	# @param [Post] self Object that invoque this method.
	#
	# @returns [NONE]
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	# Function that show the title of a post.
	#
	# @date [06/04/2017]
	#
	# @author [Chiseng Ng]
	#
	# @param [Post] self Object that invoque this method.
	#
	# @return [Post] self.title Title of the post.
	def __str__(self):
		return self.title

# Used for create user profile.
class UserProfile(models.Model):
	user = models.OneToOneField(User)