from django.db import models
import random

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
    passcode = models.CharField(max_length=4, primary_key=True)
    host = models.ForeignKey(User)

    def generate_passcode(self):
        found = True

        while found:
            code = random.randint(0, 9999)
            self.passcode = format(code, '04d')

            if Party.objects.filter(passcode=self.passcode).exists() == False:
                found = False

    def save(self, *args, **kwargs):
        self.generate_passcode()
        super(Party, self).save(*args, **kwargs)

    def __str__(self):
        return '{}: {}'.format(self.passcode, self.host)


class Playlist(models.Model):
    party = models.OneToOneField(Party, related_name='playlist')

    def __str__(self):
        return self.party.__str__()


class TrackVoting(models.Model):
    track_id = models.CharField(max_length=100)
    suggester = models.ForeignKey(User)
    votes = models.IntegerField()
    playlist = models.ForeignKey(Playlist, related_name='tracks')

    def __str__(self):
        return '{} ({} votes)'.format(self.track_id, self.votes)
