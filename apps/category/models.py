from django.db import models

from django.utils.text import slugify

from uuid import uuid4
from datetime import datetime

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Category(BaseModel):
    """
    Category model
    """

    title = models.CharField(max_length=225, unique=True, db_index=True)
    slug = models.SlugField(blank=True, db_index=True)
    parent = models.ForeignKey(
        'self', on_delete=models.CASCADE, blank=True, null=True, related_name='children', db_index=True, default=None, limit_choices_to={"parent__isnull": True}
    )
    description = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Kategoriya'
        verbose_name_plural = 'Kategoriyalar'
        ordering = ['title']

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)
        uuid_slug = str(uuid4().hex[:8])
        date_slug = datetime.today().strftime('%d-%m-%Y-%H-%M-%S')
        self.slug = f'{base_slug}-{uuid_slug}-{date_slug}'
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.title}"


class Tag(BaseModel):
    """
    Tag model
    """

    name = models.CharField(max_length=225, unique=True, db_index=True)
    slug = models.SlugField(blank=True, db_index=True)

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Taglar'
        ordering = ['-name']

    def save(self, *args, **kwargs):
        if not self.slug and self.name:
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            while Tag.objects.filter(slug=slug).exists():
                slug = f'{base_slug}-{counter}'
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
