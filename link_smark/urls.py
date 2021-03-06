"""link_smark URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
"""
from django.conf.urls import url
from django.contrib import admin


from link_smark_app.views import HomeView, UpdateB, BookmarkDetail, AddBookmark,TaggedBookmark, TaggedBookmarkView, AddTag, BookmarkList, ViewTag, ListTag, UpdateTag, TagUpdate, DetailTagView, BookmarkPostComment, PostView, NewsFeed, BookmarkPost, importHTMLasbookmarks, ViewTaggedBookmarks, GetBookmarkFromTag


urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/add/', AddBookmark.as_view(), name='bookmark'),
    url(r'^bookmark/(?P<pk>\d+)/$', AddBookmark.as_view(), name='bookmark_view'),
    url(r'^bookmark/detail/(?P<pk>\d+)/$', BookmarkDetail.as_view(), name='bookmark_detail'),
    url(r'^bookmark/details/', BookmarkDetail.as_view(), name='bookmark_list'),
    url(r'^bookmark/list/', BookmarkList.as_view(), name='list'),
    url(r'^update/(?P<pk>\d+)/$', UpdateB.as_view(), name='update'),
    url(r'^update/', UpdateB.as_view(), name='update'),
    url(r'^bookmark/tag/', AddTag.as_view(), name='tag'),
    url(r'^tag/list/', ViewTag.as_view(), name='list_tag'),

    url(r'^tag/', ListTag.as_view(), name='bookmark_tag'),
    url(r'^update_tag/', UpdateTag.as_view(), name='update_tag'),
    url(r'^tag_update/(?P<pk>\d+)/$', TagUpdate.as_view(), name='tag_update'),
    url(r'^detail_tag/(?P<pk>\d+)/$', DetailTagView.as_view(), name='detail_tag'),
    url(r'^post/$', BookmarkPostComment.as_view(), name='post'),
    url(r'^post_view/(?P<pk>\d+)/$', PostView.as_view(), name='post_view'),
    url(r'^news_feed/', NewsFeed.as_view(), name='news_feed'),
    url(r'^bookmark_post/(?P<pk>\d+)/$', BookmarkPost.as_view(), name='bookmark_post'),
    url(r'^bookmark/import/', importHTMLasbookmarks.as_view(), name='bookmark_import'),
    url(r'^bookmark/tagged', TaggedBookmarkView.as_view(), name='tagged_bookmark'),
    url(r'^tagged_bookmark/list/', ViewTaggedBookmarks.as_view(), name='list_tagged_bookmarks'),
    url(r'^bookmark/tgBook/', GetBookmarkFromTag.as_view(), name='get_bkmark_from_tg'),
    #url(r'^bookmark/tgBook/?filter=', GetBookmarkFromTag.as_view(), name='get_bkmark_from_tg'),



]
