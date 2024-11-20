from django.core.management.base import BaseCommand
from ...parser import HHParser

class Command(BaseCommand):
    help = 'Load vacancies from HH.ru API'

    def handle(self, *args, **kwargs):
        HHParser.get_all_vacancies()
        self.stdout.write(self.style.SUCCESS('Successfully loaded vacancies'))
