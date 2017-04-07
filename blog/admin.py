from django.contrib import admin
from .models import Post

# This is Django admin for manager Post
# And make our model visible
admin.site.register(Post)