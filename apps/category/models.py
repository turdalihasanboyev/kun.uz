from django.db import models
from django.utils.text import slugify

from uuid import uuid4
from datetime import datetime


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=225, unique=True)
    slug = models.SlugField(max_length=225, blank=True)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            uuid_slug = uuid4()
            date_slug = datetime.today().strftime('%d-%m-%Y-%H-%M-%S')
            self.slug = f'{base_slug}-{uuid_slug}-{date_slug}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'


class Tag(BaseModel):
    name = models.CharField(max_length=225, unique=True)
    slug = models.SlugField(max_length=225, blank=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Taglar'

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            uuid_slug = uuid4()
            self.slug = f'{base_slug}-{uuid_slug}'
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}'
