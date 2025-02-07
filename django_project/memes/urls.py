from django.urls import path

from .views import HomeView
from .views import add_meme

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/meme/', add_meme, name='meme_new'),
]
