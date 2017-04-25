# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView, UpdateView, CreateView

from .models import Bookmarks, Tag, TaggedBookmark, Posts, BookmarkComments
class HomeView(TemplateView):
    template_name='home.html'

class UpdateB(UpdateView):
    model = Bookmarks
    template_name = 'updateB.html'
    fields = ['title', 'web_url']

#class AddTag(TemplateView):
class AddTag(CreateView):
    model = Tag
    template_name = 'bookmark_tag.html'
    fields = ['text', 'description']


class TaggedBookmark(DetailView):
    model = TaggedBookmark
    template_name = 'bookmark_view_tagged.html'
    fields = ['bookmark','tag']

class AddBookmark(CreateView):

    """Add a bookmark"""
    model = Bookmarks
    template_name = 'bookmark.html'
    fields = ['title', 'web_url']
    
class BookmarkDetail(DetailView):
    model = Bookmarks
    template_name = 'bookmark_detail.html'
    fields = ['title', 'web_url', 'date']

class BookmarkList(ListView):
    model = Bookmarks
    template_name = 'bookmark_list.html'
    fields = ['title']

class BookmarkDetailView(DetailView):
    model = Bookmarks
    template_name = 'bookmark_view.html'

class ViewTag(ListView):
    model = Tag
    template_name = 'tag_list.html'
