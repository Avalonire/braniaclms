from django.db import models

"""
Реализовал абстрактный класс с настройками.
Но не получилось запихнуть туда перегрузку строки, так как в классе - Teachers - мы используем другой формат.
Оставил старую версию закомментированный на всякий случай.
"""


class OverallSettings(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    deleted = models.BooleanField(default=False, verbose_name='Удалено')

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    class Meta:
        abstract = True


class News(OverallSettings):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    preamble = models.CharField(max_length=1024, verbose_name='Вступление')

    body = models.TextField(verbose_name='Содержимое')
    body_as_markdown = models.BooleanField(default=False, verbose_name='Формат разметки Markdown')

    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    # update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # deleted = models.BooleanField(default=False, verbose_name='Удалено')
    #
    # def delete(self, *args, **kwargs):
    #     self.deleted = True
    #     self.save()

    def __str__(self):
        return f'{self.title}'

    class Meta(OverallSettings.Meta):
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Course(OverallSettings):
    title = models.CharField(max_length=256, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    cost = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Стоимость', default=0)

    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    # update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # deleted = models.BooleanField(default=False, verbose_name='Удалено')
    #
    # def delete(self, *args, **kwargs):
    #     self.deleted = True
    #     self.save()

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

    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    # update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # deleted = models.BooleanField(default=False, verbose_name='Удалено')
    #
    # def delete(self, *args, **kwargs):
    #     self.deleted = True
    #     self.save()

    def __str__(self):
        return f'{self.title}'

    class Meta(OverallSettings.Meta):
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class CourseTeacher(OverallSettings):
    courses = models.ManyToManyField(Course)
    first_name = models.CharField(max_length=256, verbose_name='Имя')
    last_name = models.CharField(max_length=256, verbose_name='Фамилия')

    # created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    # update_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    # deleted = models.BooleanField(default=False, verbose_name='Удалено')
    #
    # def delete(self, *args, **kwargs):
    #     self.deleted = True
    #     self.save()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta(OverallSettings.Meta):
        verbose_name = 'Курс к учителю'
        verbose_name_plural = 'Курсы к учителям'
