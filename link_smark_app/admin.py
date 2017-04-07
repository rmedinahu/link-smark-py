# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Posts, Bookmarks, Tag, TaggedBookmark, BookmarkComments

admin.site.register(Posts)
admin.site.register(Bookmarks)
admin.site.register(Tag)
admin.site.register(TaggedBookmark)
admin.site.register(BookmarkComments)
