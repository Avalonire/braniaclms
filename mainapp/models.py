from django.db import models
from abc import ABC, abstractmethod


class OverallSettings(ABC):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def __str__(self):
        return f'{self.title}'

    @abstractmethod
    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class News(models.Model, OverallSettings):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    preamble = models.CharField(max_length=1024, verbose_name='Вступление')

    body = models.TextField(verbose_name='Содержимое')
    body_as_markdown = models.BooleanField(default=False, verbose_name='Формат разметки Markdown')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        abstract = True


class Courses(models.Model):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость', default=0)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()


class Lesson(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, verbose_name='Курс')
    num = models.PositiveIntegerField(default=0, verbose_name='Номер урока')

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()
