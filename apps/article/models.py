from django.db import models

from django.urls import reverse

from django.utils.text import slugify
from uuid import uuid4
from datetime import datetime

# import get_user_model
from django.contrib.auth import get_user_model

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


User = get_user_model()


class Article(BaseModel):
    """
    Article model.
    """

    is_published = models.BooleanField(default=False)
    name = models.CharField(max_length=300, unique=True, db_index=True)
    slug = models.SlugField(blank=True, db_index=True)
    category = models.ForeignKey(
        "category.Category", on_delete=models.CASCADE, related_name="article_category"
    )
    tags = models.ManyToManyField("category.Tag", related_name="article_tags", blank=True)
    content = RichTextField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_author")
    painter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="article_painter")
    image = models.ImageField(
        upload_to="article_images", default='img/default.png')
    video = models.FileField(upload_to="article_videos", blank=True, null=True)
    duration = models.DurationField(null=True, blank=True)
    read_time = models.DurationField(null=True, blank=True) # duration field yangi
    published_at = models.DateTimeField(auto_now_add=True)
    views = models.BigIntegerField(default=0)

    class Meta:
        ordering = ["-published_at"]
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"

    def get_absolute_url(self, *args, **kwargs):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        base_slug = slugify(self.name)
        uuid_slug = uuid4()
        # date_slug = datetime.today().strftime('%d-%m-%Y-%H-%M-%S') # yuqori darajada unikal va lokal timezone ni qo'llamaydi
        date_slug = datetime.now().strftime('%d-%m-%Y') # pastroq darajada unikal va lokal timezone ni qo'llaydi
        self.slug = f"{base_slug}-{uuid_slug}-{date_slug}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"
