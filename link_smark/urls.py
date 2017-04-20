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
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from link_smark_app.views import HomeView, UpdateB, BookmarkDetail, AddBookmark, BookmarkList

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^admin/', admin.site.urls),
url(r'^bookmark/list/', BookmarkList.as_view(), name='list'),
    url(r'^update/(?P<pk>\d+)/$', UpdateB.as_view(), name='update'),
    url(r'^bookmark/add/', AddBookmark.as_view(), name='bookmark'),
    url(r'^bookmark/detail/(?P<pk>\d+)/$', BookmarkDetail.as_view(), name='bookmark_detail'),
    

]
