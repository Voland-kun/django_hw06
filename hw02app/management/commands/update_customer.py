from django.core.management.base import BaseCommand
from ...models import Customer


class Command(BaseCommand):
    help = 'Update customer'

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Client id')
        parser.add_argument('--name', type=str, help='New name')
        parser.add_argument('--email', type=str, help='New email')
        parser.add_argument('--address', type=str, help='New address')
        parser.add_argument('--phone', type=str, help='New phone number')

    def handle(self, *args, **kwargs):
        customer = Customer.objects.get(pk=kwargs['pk'])
        if customer is not None:
            customer.name = kwargs['name']
            customer.email = kwargs['email']
            customer.address = kwargs['address']
            customer.phone = kwargs['phone']
        customer.save()
        self.stdout.write(f'Customer {customer.pk} updated')
