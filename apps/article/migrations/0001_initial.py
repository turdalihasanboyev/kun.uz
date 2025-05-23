# Generated by Django 5.2 on 2025-05-07 16:18

import ckeditor.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=300, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=300)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image', models.ImageField(default='img/default.png', upload_to='article_images')),
                ('video', models.FileField(blank=True, null=True, upload_to='article_videos')),
                ('duration', models.DurationField(blank=True, null=True)),
                ('read_time', models.DurationField(blank=True, null=True)),
                ('views', models.BigIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_category', to='category.category')),
                ('painter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_painter', to=settings.AUTH_USER_MODEL)),
                ('tags', models.ManyToManyField(blank=True, related_name='article_tags', to='category.tag')),
            ],
            options={
                'verbose_name': 'Maqola',
                'verbose_name_plural': 'Maqolalar',
            },
        ),
    ]
