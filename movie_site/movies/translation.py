from django.contrib import admin
from .models import *
from modeltranslation.translator import TranslationOptions, register



@register(Movie)
class ProductTranslationOptions(TranslationOptions):
    fields = ('movie_name', 'description')