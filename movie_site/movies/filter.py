from django_filters.rest_framework import FilterSet
from .models import *


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'release_date': ['exact'],
            'genres': ['exact'],
            'country': ['exact'],
            # 'rating__stars': ['gt', 'lt'],
        }