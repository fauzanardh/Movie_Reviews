from django.contrib import admin
from movie_reviews.models import Movies, Reviews


class MoviesAdminModel(admin.ModelAdmin):
    list_display = ('name', 'synopsis')
    list_filter = ('name',)


class ReviewsAdminModel(admin.ModelAdmin):
    list_display = ('text', 'star_rating', 'created_by', 'movie')
    list_filter = ('movie', 'created_by')


admin.site.register(Movies, MoviesAdminModel)
admin.site.register(Reviews, ReviewsAdminModel)
