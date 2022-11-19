from django.contrib import admin
from django.utils.html import format_html

from mainapp.models import News, Course, CourseTeacher, Lesson

# admin.site.register(News)
admin.site.register(Course)
admin.site.register(CourseTeacher)
admin.site.register(Lesson)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'deleted',)
    # Фильтр по удаленному или дате создания
    list_filter = ('deleted', 'created_at',)
    # Сортировка по primary key
    ordering = ('pk',)
    # Пагинатор
    list_per_page = 2
    # Поле поиска, регистрозависимое (что бы это изменить, надо переназначить метод Search)
    search_fields = ('title', 'intro', 'body',)
    actions = ('mark_as_delete',)

    def slug(self, obj):
        return format_html(
            '<a href="{}" target="_blank">{}</a>',
            obj.title.lower().replace(' ', '-'),
            obj.title
        )

    slug.short_description = 'Слаг'

    def mark_as_delete(self, request, queryset):
        queryset.update(deleted=True)

    mark_as_delete.short_description = 'Пометить удаленным'
