from rest_framework import serializers
from .models import Genre, Movie, Score


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'audience', 'poster_url', 'description', 'genre']
        
class GenreSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(source="movie_set", many=True, read_only=True)
    class Meta:
        model = Genre
        fields = ['id', 'name', 'movies']
        
class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = ['id', 'content', 'score']
        
