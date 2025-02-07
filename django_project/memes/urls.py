from django.urls import path

from .views import HomeView, MemeCreateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('add/meme/', MemeCreateView.as_view(), name='meme_new'),
]
