from django.core.management.base import BaseCommand
from ...models import Customer


class Command(BaseCommand):
    help = 'Add customer'

    def add_arguments(self, parser):
        parser.add_argument('--name', type=str, help='New name')
        parser.add_argument('--email', type=str, help='New email')
        parser.add_argument('--address', type=str, help='New address')
        parser.add_argument('--phone', type=str, help='New phone number')

    def handle(self, *args, **kwargs):
        customer = Customer(name=kwargs['name'],
                            email=kwargs['email'],
                            address=kwargs['address'],
                            phone=kwargs['phone'])
        customer.save()
        self.stdout.write(f'{customer}')
