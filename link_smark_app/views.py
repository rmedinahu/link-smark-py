# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.urls import reverse

from django import forms

from django.shortcuts import render

from django.views.generic import TemplateView, DetailView, ListView, UpdateView, CreateView, FormView

from .models import Bookmarks, Tag, TaggedBookmark, Posts

from .htmlparser import MyHTMLParser

class UploadFileForm(forms.Form):
    file = forms.FileField()

class HomeView(TemplateView):
    template_name='home.html'

class UpdateB(UpdateView):
    model = Bookmarks
    template_name = 'updateB.html'
    fields = ['title', 'web_url']


class AddTag(CreateView):
    model = Tag
    template_name = 'bookmark_tag.html'
    fields = ['text', 'description']


class TaggedBookmarkView(CreateView):
    model = TaggedBookmark
    template_name = 'bookmark_view_tagged.html'
    fields = ['bookmark','tag']

    def get_success_url(self):
        return reverse('list_tagged_bookmarks')


class ViewTaggedBookmarks(ListView):
    model = TaggedBookmark
    template_name = 'view_tagged_bookmark.html'

class GetBookmarkFromTag(TemplateView):
    template_name = 'get_bookmark_from_tag.html'

    def get_context_data(self, **kwargs):
        context = super(GetBookmarkFromTag, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        if self.request.GET:
            tag_filter = self.request.GET.get('filter')
            tagged = TaggedBookmark.objects.filter(tag__text=tag_filter)
            context['bookmarks'] = tagged
        return context


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

class ListTag(ListView):
    model = Tag 
    template_name = 'bookmark_tag.html'
    fields = ['text', 'description']

class UpdateTag(ListView):
    model = Tag
    template_name = 'update_tag.html'
    fields = ['text', 'description']

class TagUpdate(UpdateView):
    model = Tag
    template_name = 'tag_update.html'
    fields = ['text', 'description']

class DetailTagView(DetailView):
    model = Tag
    template_name = 'detail_tag.html'
    fields = ['text', 'description']

class BookmarkPostComment(CreateView):
    model = Posts
    template_name = 'post.html'
    fields = ['creator', 'msg']

class PostView(DetailView):
    model = Posts
    template_name = 'post_view.html'

class NewsFeed(ListView):
    model = Posts
    template_name = 'news_feed.html'
#
class BookmarkPost(UpdateView):
    model = Posts
    template_name = 'bookmark_post.html'
    fields = ['bookmark']


    def get_success_url(self):
        return reverse('bookmark_post')
class importHTMLasbookmarks (FormView):
    template_name = 'bookmark_import.html'
    form_class = UploadFileForm
    success_url = "/bookmark/list/"
    def form_valid(self, form):
        file = self.request.FILES['file']
        m = MyHTMLParser()
        line = str(file.read())
        m.feed(line)
        name = m.namez()
        attr = m.attrits()
        for i in range(len(name)):
            newbk = Bookmarks(title = name[i], web_url = attr[i])
            newbk.save()
        return super(importHTMLasbookmarks, self).form_valid(form)
