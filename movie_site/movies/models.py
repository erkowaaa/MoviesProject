from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=16)
    phone_number = PhoneNumberField(unique=True)
    STATUS_CHOICES = (
        ('pro', 'Pro'),
        ('simple', 'Simple')
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='simple')


    def __str__(self):
        return self.nickname


class Country(models.Model):
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name


class Director(models.Model):
    director_name = models.CharField(max_length=32)
    bio = models.TextField()
    age = models.PositiveIntegerField(default=0, null=True, blank=True)
    director_image = models.ImageField(upload_to='direstor_images/')

    def __str__(self):
        return self.director_name


class Actor(models.Model):
    actor_name = models.CharField(max_length=32)
    bio = models.TextField()
    age = models.PositiveIntegerField(default=0, null=True, blank=True)
    actor_image = models. ImageField(upload_to='actor_images/')

    def __str__(self):
        return self.actor_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.genre_name


class Movie(models.Model):
    TYPE_CHOICES = [
        ('144', '144p'),
        ('360', '360p'),
        ('480', '480p'),
        ('720', '720p'),
        ('1080', '1080p'),
        ('1080 Ultra', '1080 Ultra'),
    ]

    STATUS_CHOICES = [
        ('Pro', 'Pro'),
        ('Simple', 'Simple'),
    ]

    movie_name = models.CharField(max_length=100)
    release_date = models.DateField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    actors = models.ManyToManyField(Actor, related_name='movies')
    genres = models.ManyToManyField(Genre, related_name='movies')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    movie_time = models.SmallIntegerField()
    description = models.TextField()
    movie_trailer = models.FileField(upload_to='movies/trailer/', null=True, blank=True)
    movie_image = models.ImageField(upload_to='movies/images/', null=True, blank=True)
    movie_file = models.FileField(upload_to='movies/files/', null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Simple')
    owner = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_name

    def get_average_rating(self):
        ratings = self.ratings.all()
        if ratings.exists():
            return round(sum(rating.stars for rating in ratings) / ratings.count(), 1)
        return 0


class Rating(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, related_name='ratings', on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1, 11)])

    def __str__(self):
        return f"{self.stars} stars for {self.movie.movie_name} by {self.user.nickname}"


class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.nickname} on {self.movie.movie_name}"

