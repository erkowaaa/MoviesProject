from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
from django.contrib.admin import AdminSite


class MyAdminSite(AdminSite):
    site_header = 'Cinema Administration'

    def each_context(self, request):
        context = super().each_context(request)
        context['custom_css'] = 'css/admin_custom.css'
        return context


admin_site = MyAdminSite()


@admin.register(Movie)
class MovieAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),

        }


admin.site.register(UserProfile)
admin.site.register(Country)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Rating)
admin.site.register(Comment)

