from rest_framework import serializers
from boppable.models import Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'trackID', 'indexID', 'startPosition')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name')