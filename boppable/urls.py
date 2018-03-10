from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from boppable import views

urlpatterns = [
    url(r'^boppable/$', views.SongList.as_view()),
    url(r'^boppable/(?P<pk>[0-9]+)/$', views.SongDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)