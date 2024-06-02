from django.contrib import admin
from .models import Movie
from .models import Review,Like
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Like)


# Register your models here.
