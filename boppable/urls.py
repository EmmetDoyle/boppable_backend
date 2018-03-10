from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from boppable import views

urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^users/$', views.UserCreate.as_view(), name='users-create'),
    url(r'^parties/$', views.PartyCreate.as_view(), name='parties-create'),
    url(r'^parties/(?P<pk>[0-9]{4})/$', views.PartyDetail.as_view(), name='parties-detail'),
    url(r'^trackvoting/$', views.TrackVotingCreate.as_view(), name='trackvoting-create'),
    url(r'^trackvoting/exists/$', views.does_track_voting_exist),
    url(r'^trackvoting/(?P<pk>[0-9]+)/upvote$', views.track_voting_upvote),
    url(r'^trackvoting/(?P<pk>[0-9]+)/downvote$', views.track_voting_downvote),
]
urlpatterns = format_suffix_patterns(urlpatterns)