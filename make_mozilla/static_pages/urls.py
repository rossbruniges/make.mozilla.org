from django.conf.urls.defaults import patterns, url
from make_mozilla.static_pages import views

urlpatterns = patterns('',
    url(r'^videos/$', views.webmaker_videos, name='webmaker_videos'),
    url(r'^hall-of-fame/$', views.webmaker_hoc,     name='webmaker_hoc'),
    url(r'^ITU/$', views.itu_index, name='itu_index'),
    url(r'^ITU/kit/$', views.itu_kit, name='itu_kit'),
    url(r'^ITU/advocates/$', views.itu_advocates, name='itu_advocates'),
    url(r'^ITU/videos/$', views.itu_videos, name='itu_videos'),
)
