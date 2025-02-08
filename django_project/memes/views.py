from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.db.models import Q
from django.conf import settings

from .models import Meme, Tag
from .forms import MemeForm, TagFormSet
from .imagga import ImaggaService


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
            imagga = ImaggaService(settings.IMAGGA_API_KEY, settings.IMAGGA_API_SECRET)
            print('Imagga Service: ', imagga.analyze_image(meme.image.path))

            tags = formset.save(commit=False)
            tags_imagga = imagga.analyze_image(meme.image.path)

            for tag_name, confidence in tags_imagga:
                Tag.objects.create(meme_id=meme, tag=tag_name, confianza=confidence)

            for tag in tags:
                tag.meme_id = meme
                tag.save()

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


class SearchResultsListView(ListView):
    model = Meme
    context_object_name = 'memes'
    template_name = 'memes/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')

        if query:
            return Meme.objects.filter(
                Q(description__icontains=query) |
                Q(id__in=Tag.objects.filter(tag__icontains=query).values_list('meme_id', flat=True))
            ).distinct()
        return Meme.objects.all()
