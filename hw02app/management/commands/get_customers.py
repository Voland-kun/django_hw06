from django.core.management.base import BaseCommand
from ...models import Customer


class Command(BaseCommand):
    help = 'Get customers'

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()
        for customer in customers:
            self.stdout.write(f'{customer}')