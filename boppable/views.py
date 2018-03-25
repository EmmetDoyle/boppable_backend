from rest_framework import generics
# from boppable.models import *
from boppable.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('users-create', request=request, format=format),
        'parties': reverse('parties-create', request=request, format=format),
        'trackvoting': reverse('trackvoting-create', request=request, format=format)
    })

class SongList(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SongDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PartyCreate(generics.CreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class PartyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class TrackVotingCreate(generics.CreateAPIView):
    queryset = TrackVoting.objects.all()
    serializer_class = TrackVotingCreateSerializer


class TrackVotingDelete(generics.DestroyAPIView):
    queryset = TrackVoting.objects.all()
    serializer_class = TrackVotingGetSerializer


@csrf_exempt
def track_voting_upvote(request, pk):
    trackvoting = TrackVoting.objects.get(pk=pk)
    trackvoting.votes += 1

    trackvoting.save()

    return HttpResponse(status=204)


@csrf_exempt
def track_voting_downvote(request, pk):
    trackvoting = TrackVoting.objects.get(pk=pk)
    trackvoting.votes -= 1

    trackvoting.save()

    return HttpResponse(status=204)


@csrf_exempt
def does_track_voting_exist(request):
    track_id = request.POST['track_id']
    playlist = request.POST['playlist']

    exists = TrackVoting.objects.filter(playlist_id=playlist, track_id=track_id).exists()

    return JsonResponse({'exists': exists})
