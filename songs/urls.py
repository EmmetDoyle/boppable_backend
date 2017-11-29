from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from songs import views

urlpatterns = [
    url(r'^songs/$', views.SongList.as_view()),
    url(r'^songs/(?P<pk>[0-9]+)/$', views.SongDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)