from django import forms
from django.forms import inlineformset_factory

from .models import Meme, Tag

class MemeForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-textarea rounded-md border border-slate-600',
                'rows': 3
            }),
            'image': forms.FileInput(attrs={
                'accept': 'image/*',
                'class': 'file:mr-4 file:rounded-full file:border-0 file:bg-violet-50 file:px-4 file:py-2 file:text-sm file:font-semibold file:text-violet-700 hover:file:bg-violet-100 dark:file:bg-violet-600 dark:file:text-violet-100 dark:hover:file:bg-violet-500 ...'
            }),
            'user': forms.TextInput(attrs={
                'class': 'form-input rounded-md border border-slate-600'
            })
        }

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag']
        widgets = {
            'tag': forms.TextInput(attrs={
                'class': 'form-input rounded-md border border-slate-600'
            })
        }
TagFormSet = inlineformset_factory(
    Meme,
    Tag,
    form=TagForm,
    extra=1,
    can_delete=True
)
