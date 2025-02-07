from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Meme
from .forms import MemeForm

# Create your views here.
class HomeView(ListView):
    model = Meme
    context_object_name = 'memes'
    template_name = 'index.html'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tags').all()

class MemeCreateView(CreateView):
    model = Meme
    template_name = 'memes/meme_new.html'
    form_class = MemeForm
    success_url = reverse_lazy('home')

