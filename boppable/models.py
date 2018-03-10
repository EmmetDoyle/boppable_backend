from django.db import models

class Song(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    trackID = models.CharField(max_length=100, blank=True, default='')
    indexID = models.IntegerField(blank=False, default=0)
    startPosition = models.IntegerField(blank=False, default=0)

    class Meta:
        ordering = ('created',)


class User(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Party(models.Model):
    passcode = models.CharField(max_length=4)
    host = models.ForeignKey(User)

    def __str__(self):
        return '{}: {}'.format(self.passcode, self.host)


class Track(models.Model):
    track_id = models.CharField(max_length=100)


class TrackRequest(models.Model):
    track = models.ForeignKey(Track)
    suggester = models.ForeignKey(User)
    party = models.ForeignKey(Party, related_name='tracks')

    def __str__(self):
        return '{}: {} {}'.format(self.suggester, self.track_id, self.party)


class Playlist(models.Model):
    party = models.OneToOneField(Party, related_name='playlist')

    def __str__(self):
        return self.party


class TrackVoting(models.Model):
    track = models.ForeignKey(TrackRequest)
    votes = models.IntegerField()
    playlist = models.ForeignKey(Playlist, related_name='tracks')

    def __str__(self):
        return '{} ({} votes)'.format(self.track, self.votes)
