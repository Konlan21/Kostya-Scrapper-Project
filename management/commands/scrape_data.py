

from django.core.management.base import BaseCommand
from scrapy import cmdline

class Command(BaseCommand):
    help = 'Run Scrapy spiders'

    def handle(self, *args, **options):
        cmdline.execute(['scrapy', 'crawl', 'your_spider_name'])
        # Repeat the above line for each spider you want to run
