from django.urls import path
from .services import scrape

urlpatterns = [
    path('', scrape, name='scrape'),
]