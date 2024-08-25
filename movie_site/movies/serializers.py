from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'nickname', 'email', 'password', 'phone_number', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validates_date):
        user = UserProfile.objects.create_user(**validates_date)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password']



class LoginSerializer(serializers.Serializer):
    user_name = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, date):
        user = authenticate(**date)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = '__all__'


class DirectorSerializerSimple(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = ['director_name']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class ActorSerializerSimple(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = ['actor_name']


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class GenreSerializerSimple(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['genre_name']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()
    ratings = RatingSerializer(many=True, read_only=True,)

    class Meta:
        model = Movie
        fields = ['movie_name', 'movie_image', 'average_rating', 'release_date', 'country', 'genres', 'ratings']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class MovieSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    director = DirectorSerializerSimple()
    actors = ActorSerializerSimple(many=True, read_only=True)
    genres = GenreSerializerSimple(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    ratings = RatingSerializer(many=True, read_only=True)
    owner = UserProfileSerializer()

    class Meta:
        model = Movie
        fields = ['movie_name', 'release_date', 'country', 'director', 'actors', 'genres', 'type', 'movie_time', 'description',
                  'movie_trailer', 'movie_image', 'movie_file', 'average_rating', 'status', 'ratings', 'owner']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'