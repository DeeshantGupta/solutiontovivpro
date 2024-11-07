from rest_framework import generics, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer
from django.shortcuts import render


# Create your views here.


#First endpoint - To get all songs with pagination
class SongListView(generics.ListAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer

#Second endpoint - get song by title 
@api_view(['GET'])
def get_song_by_title(request, title):
    try:
        song = Song.objects.get(title=title)
        serializer = SongSerializer(song)
        return Response(serializer.data)
    except:
        return Response({"error": "Song not found"}, status=status.HTTP_404_NOT_FOUND)

#Third endpoint - for rating
@api_view(['POST'])
def rate_song(request, title):
    try:
        song = Song.objects.get(title=title)
        rating=request.data.get('star_rating')
        try:
            rating = float(rating)
        except:
            return Response({"error": "Invalid rating"}, status=status.HTTP_400_BAD_REQUEST)

        if 0<=rating and rating<=5:
            print("HERE")
            song.star_rating = rating
            song.save()
            return Response({"message":"Rating updated successfully"})
        else:
            return Response({"error": "Invalid rating"}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'error':'Song not found'}, status=status.HTTP_404_NOT_FOUND)