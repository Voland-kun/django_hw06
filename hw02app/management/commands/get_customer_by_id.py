from django.core.management.base import BaseCommand
from ...models import Customer


class Command(BaseCommand):
    help = 'Get customer by id'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User id')

    def handle(self, *args, **options):
        customer = Customer.objects.get(pk=options['pk'])
        self.stdout.write(f'{customer}')