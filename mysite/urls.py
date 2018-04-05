"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from comics import views as comics_views
urlpatterns = [
    url(r'^time/', comics_views.current_datetime),

    url(r'^comics/$',comics_views.index),

    url(r'^$', comics_views.comicslist),



    url(r'^comics/comiclist/$', comics_views.comicslist),
    url(r'^comics/comicinfo/(.*)/$', comics_views.comicsinfo, name="comicinfo"),
    url(r'^comics/comic/(.*)/(.*)/(.*)/$', comics_views.comicsview, name="comicview"),
    url(r'^comics/comicpage/(.*)/(.*)/(.*)$', comics_views.comicspage, name="comicpage"),





    url(r'^admin/', admin.site.urls),
]
