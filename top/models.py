from tkinter import Image

from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=100)


def val_title(value):
    if 'nurik' in value:
        raise ValidationError(message="Зоголовок содержит цинзурные слова")


class Top(models.Model):
    title = models.CharField(max_length=100, validators=[val_title])
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    types = models.ManyToManyField(Type, related_name='tops')
    image = models.ImageField(upload_to='images/')


