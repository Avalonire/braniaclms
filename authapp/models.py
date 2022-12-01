from django.db import models
from django.contrib.auth.models import AbstractUser
from mainapp.models import NULLABLE


class User(AbstractUser):
    email = models.EmailField(verbose_name='Email', blank=True, unique=True)
    age = models.PositiveSmallIntegerField(verbose_name='возраст', **NULLABLE)
    avatar = models.ImageField(upload_to='users', **NULLABLE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
