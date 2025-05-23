# Generated by Django 5.2 on 2025-05-07 16:18

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=225)),
                ('email', models.EmailField(max_length=225)),
                ('phone_number', models.CharField(max_length=225)),
                ('subject', models.CharField(max_length=225)),
                ('message', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='contact_files/')),
            ],
            options={
                'verbose_name': 'Aloqa',
                'verbose_name_plural': 'Aloqalar',
            },
        ),
    ]
