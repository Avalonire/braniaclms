from django.core.management import BaseCommand
from mainapp.models import News


class Command(BaseCommand):

    def handle(self, *args, **options):
        news_object = []
        for i in range(10):
            news_object.append(
                News(
                    title=f'news#{i}',
                    preamble=f'preamble#{i}',
                    body=f'New text test message'
                )
            )
        News.objects.bulk_create(news_object)
