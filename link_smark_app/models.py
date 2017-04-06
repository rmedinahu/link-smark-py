# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#user class that handles all users
class User(models.Model): 
	usr_name = models.CharField(max_length=255)
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	interests = models.CharField(max_length=255)

	def __str__(self):
		return self.usr_name

#post class that handles user publications
class Posts(models.Model):
	usr_post = models.URLField(max_length=255)
	usr_post_msg = models.CharField(max_length=255)
	post_date = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.usr_post

#bookmark class that contains all bookmarks
class Bookmarks(models.Model):
	bkmark_title = models.CharField(max_length=255)
	bkmark_address = models.URLField(max_length=255)
	bkmark_date = models.DateTimeField(max_length=255)

	def __str__(self):
		return self.bkmark_title 

#class for tagging bookmarks with description
class Tag(models.Model):
	tag_keywrd = models.CharField(max_length=255)
	tag_description = models.CharField(max_length=255)
	
	def __str__(self):
		return self.tag_keywrd 		
