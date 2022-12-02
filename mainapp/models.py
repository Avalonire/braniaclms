from django.conf import settings
from django.db import models

"""
Реализовал абстрактный класс с настройками.

"""

NULLABLE = {'blank': True, 'null': True}


class OverallSettings(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    class Meta:
        abstract = True
        ordering = ('-created_at',)


class News(OverallSettings):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    preamble = models.CharField(max_length=1024, verbose_name='Вступление')

    body = models.TextField(verbose_name='Содержимое')
    body_as_markdown = models.BooleanField(default=False, verbose_name='Формат разметки Markdown')

    def __str__(self):
        return f'{self.title}'

    class Meta(OverallSettings.Meta):
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Course(OverallSettings):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta(OverallSettings.Meta):
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(OverallSettings):
    courses = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    num = models.PositiveIntegerField(default=0, verbose_name='Номер урока')

    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta(OverallSettings.Meta):
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'


class CourseTeacher(OverallSettings):
    courses = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta(OverallSettings.Meta):
        verbose_name = 'Курс к учителю'
        verbose_name_plural = 'Курсы к учителям'


class CourseFeedback(OverallSettings):
    RATINGS_FIVE = 5

    RATINGS = (
        (RATINGS_FIVE, '☆☆☆☆☆'),
        (4, '☆☆☆☆'),
        (3, '☆☆☆'),
        (2, '☆☆'),
        (1, '☆'),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Курс')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')
    rating = models.PositiveSmallIntegerField(choices=RATINGS, default=RATINGS_FIVE, verbose_name='Рейтинг')
    feedback = models.TextField(default='Без отзыва', verbose_name='Отзыв')

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'Отзыв на {self.course} от {self.user}'
