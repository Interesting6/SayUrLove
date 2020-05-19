"""toMyLover URL Configuration

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

from hpBirthDApp import views as hpBirthD
from . import settings
from django.conf.urls.static import static, serve
# static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', hpBirthD.login),
    url(r'^birthday$', hpBirthD.cake),
    url(r'^memories$', hpBirthD.memo),
    url(r'^index/$', hpBirthD.home_page),
    url(r'^play/$', hpBirthD.play_video),
    url(r'^page1/$', hpBirthD.page1),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT, }, name='static'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }, name='media'),
]
