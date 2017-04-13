# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView

from .models import Bookmarks

class HomeView(TemplateView):
    template_name='home.html'



class AddBookmark(CreateView):
	"""Add a bookmark"""
	model = Bookmarks
	template_name = 'bookmark.html'
	fields = ['title', 'web_url']
