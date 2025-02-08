from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from .models import Meme
from .forms import MemeForm, TagFormSet

# Create your views here.
class HomeView(ListView):
    model = Meme
    context_object_name = 'memes'
    template_name = 'index.html'

    def get_queryset(self):
        return super().get_queryset().prefetch_related('tags').all()


def add_meme(request):
    if request.method == 'POST':
        meme_form = MemeForm(request.POST, request.FILES)
        formset = TagFormSet(request.POST)
        if meme_form.is_valid() and formset.is_valid():
            meme = meme_form.save()
            tags = formset.save(commit=False)
            for tag in tags:
                tag.meme_id = meme
                tag.save()
            formset.save_m2m()
            return redirect('home')
        else:
            print(f'Errores en el formulario: {meme_form.errors}, {formset.errors}')
    else:
        meme_form = MemeForm()
        formset = TagFormSet()

    return render(request, 'memes/meme_new.html', {
        'meme_form': meme_form,
        'formset': formset
    })
