from django.db import models

from ckeditor.fields import RichTextField

from apps.common.models import BaseModel


class Contact(BaseModel):
    name = models.CharField(max_length=225, db_index=True)
    email = models.EmailField(max_length=225, db_index=True, unique=True)
    phone_number = models.CharField(max_length=225, db_index=True, unique=True)
    subject = models.CharField(max_length=225, db_index=True, unique=True)
    message = RichTextField(null=True, blank=True)
    file = models.FileField(upload_to='contact_files/', null=True, blank=True)

    class Meta:
        verbose_name = 'Aloqa'
        verbose_name_plural = 'Aloqalar'

    def __str__(self):
        return f'{self.name} - {self.subject}'
