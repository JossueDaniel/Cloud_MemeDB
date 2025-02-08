from django.urls import path

from .views import HomeView, SearchResultsListView
from .views import add_meme

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/meme/', add_meme, name='meme_new'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
