from rest_framework import serializers
from boppable.models import *


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'trackID', 'indexID', 'startPosition')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name',)


class TrackVotingSerializer(serializers.ModelSerializer):
    suggester = UserSerializer()

    class Meta:
        model = TrackVoting
        fields = ('track_id', 'votes', 'playlist', 'suggester')


class PlaylistSerializer(serializers.ModelSerializer):
    tracks = TrackVotingSerializer(many=True)

    class Meta:
        model = Playlist
        fields = ('party', 'tracks')


class PartySerializer(serializers.ModelSerializer):
    playlist = PlaylistSerializer()

    class Meta:
        model = Party
        fields = ('passcode', 'host', 'playlist')
        read_only_fields = ('passcode', 'playlist')