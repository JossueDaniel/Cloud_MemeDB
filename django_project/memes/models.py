import uuid

from django.db import models

# Create your models here.
class Meme(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
    image = models.ImageField(upload_to='memes/')
    user = models.CharField(max_length=50, blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Imagen {self.id}'

class Tag(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    meme_id = models.ForeignKey(Meme, on_delete=models.CASCADE, related_name='tags')
    tag = models.CharField(max_length=100, unique=True)
    confianza = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ['tag']
        indexes = [
            models.Index(fields=['tag']),
        ]
        verbose_name = 'tag'
        verbose_name_plural = 'tags'

    def __str__(self):
        return self.tag
