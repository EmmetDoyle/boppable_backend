from rest_framework import serializers
from boppable.models import *


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'trackID', 'indexID', 'startPosition')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name',)


class TrackVotingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackVoting
        fields = ('id', 'track_id', 'votes', 'playlist', 'suggester')


class TrackVotingGetSerializer(serializers.ModelSerializer):
    suggester = UserSerializer()

    class Meta:
        model = TrackVoting
        fields = ('id', 'track_id', 'votes', 'playlist', 'suggester')


class PlaylistSerializer(serializers.ModelSerializer):
    tracks = TrackVotingGetSerializer(many=True)

    class Meta:
        model = Playlist
        fields = ('id', 'party', 'tracks')


class PartySerializer(serializers.ModelSerializer):
    playlist = PlaylistSerializer()

    class Meta:
        model = Party
        fields = ('passcode', 'host', 'playlist')
        read_only_fields = ('passcode', 'playlist')
