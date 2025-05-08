from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth import get_user_model

from uuid import uuid4
from datetime import datetime

from ckeditor.fields import RichTextField

from apps.category.models import BaseModel


User = get_user_model()


class Article(BaseModel):
    is_published = models.BooleanField(default=False)
    name = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, blank=True)
    category = models.ForeignKey(
        "category.Category", on_delete=models.CASCADE, related_name="article_category"
    )
    tags = models.ManyToManyField(
        "category.Tag", related_name="article_tags", blank=True)
    content = RichTextField(null=True, blank=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_author")
    painter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="article_painter")
    image = models.ImageField(
        upload_to="article_images", default='img/default.png')
    video = models.FileField(upload_to="article_videos", blank=True, null=True)
    duration = models.DurationField(null=True, blank=True)
    read_time = models.DurationField(
        null=True, blank=True)
    views = models.BigIntegerField(default=0)

    class Meta:
        verbose_name = 'Maqola'
        verbose_name_plural = 'Maqolalar'

    def get_absolute_url(self, *args, **kwargs):
        return reverse('article-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            uuid_slug = uuid4()
            date_slug = datetime.now().strftime('%d-%m-%Y')
            self.slug = f'{base_slug}-{uuid_slug}-{date_slug}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
