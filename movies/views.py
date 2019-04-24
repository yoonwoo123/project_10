from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Genre, Movie, Score
from .serializers import GenreSerializer, MovieSerializer, ScoreSerializer

# Create your views here.
@api_view(['GET'])
def genre_list(request):
    '''
    장르 목록
    '''
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def genre_detail(request, genre_pk):
    '''
    장르 상세 페이지
    '''
    genre = get_object_or_404(Genre, pk=genre_pk)
    serializer = GenreSerializer(genre)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list(request):
    '''
    영화 목록
    '''
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    '''
    영화 상세 페이지
    '''
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['POST'])
def score_new(request, movie_pk):
    '''
    평점 등록
    '''
    serializer = ScoreSerializer(data = request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie_id=movie_pk)
        return Response({'message': '작성되었습니다.'})
        
@api_view(['PUT', 'DELETE'])
def score_edit_delete(request, movie_pk, score_pk):
    '''
    평점 수정 및 삭제
    '''
    score = get_object_or_404(Score, pk=score_pk)
    if request.method=="PUT":
        serializer = ScoreSerializer(data = request.data, instance = score)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': '수정되었습니다.'})
    else:
        score.delete()
        return Response({'message': '삭제되었습니다.'})