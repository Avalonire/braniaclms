# Generated by Django 4.1.2 on 2022-11-19 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='возраст'),
        ),
    ]
