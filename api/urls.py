from django.urls import path
from .services import search, get_chapter, get_image

urlpatterns = [
    path('search', search, name='search'),
    path('chapter/<path:id>', get_chapter, name='chapter'),
    path('image/<path:id>', get_image, name='image'),
]