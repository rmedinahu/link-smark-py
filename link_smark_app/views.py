# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView, UpdateView

from django.views.generic import TemplateView, DetailView, ListView, CreateView

from .models import Bookmarks

class HomeView(TemplateView):
    template_name='home.html'

class UpdateB(UpdateView):
    model = Bookmarks
    template_name = 'updateB.html'
    fields = ['title', 'web_url']

class AddBookmark(CreateView):
	"""Add a bookmark"""
	model = Bookmarks
	template_name = 'bookmark.html'
	fields = ['title', 'web_url']

class BookmarkDetail(DetailView):
    model = Bookmarks
    template_name = 'bookmark_detail.html'

class BookmarkDetailView(DetailView):
    model = Bookmarks
    template_name = 'bookmark_view.html'
