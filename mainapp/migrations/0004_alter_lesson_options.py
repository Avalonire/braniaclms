# Generated by Django 4.1.2 on 2022-11-25 18:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_course_options_alter_courseteacher_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'ordering': ('-created_at',), 'verbose_name': 'lesson', 'verbose_name_plural': 'lessons'},
        ),
    ]
