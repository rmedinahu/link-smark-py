# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse
# Use django's built in User class.
from django.contrib.auth.models import User


class Posts(models.Model):
	"""post class that handles user messages about bookmarks. 
	"""
	creator = models.ForeignKey(User)
	msg = models.TextField(max_length=255)
	date = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.msg


class Bookmarks(models.Model):
	"""bookmark class that contains all bookmarks
	"""
	title = models.CharField(max_length=255)
	web_url = models.URLField()
	date = models.DateTimeField(auto_now=True)

	def get_absolute_url(self):
		return reverse('bookmark_view', kwargs={'pk': self.pk})

	def __str__(self):
		return self.title 


class Tag(models.Model):
	"""class for tagging bookmarks with description
	"""
	text = models.CharField(max_length=255, unique=True)
	description = models.CharField(max_length=255)
	
	def __str__(self):
		return self.text


class TaggedBookmark(models.Model):
	bookmark = models.ForeignKey(Bookmarks, related_name="tags")
	tag = models.ForeignKey(Tag, related_name="tagged_bkmarks")



class BookmarkComments(models.Model):	
	bookmark = models.ForeignKey(Bookmarks)
	post = models.ForeignKey(Posts)
