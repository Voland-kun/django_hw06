from django.core.management.base import BaseCommand
from ...models import Customer, Product, Order
import random
from faker import Faker


class Command(BaseCommand):
    help = 'Fake data'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):
            Customer.objects.create(
                name=fake.name(),
                email=fake.email(),
                phone=fake.phone_number(),
                address=fake.address(),
            )

        for _ in range(20):
            Product.objects.create(
                name=fake.word(),
                description=fake.text(),
                price=random.uniform(1, 1000),
                quantity=random.randint(1, 100),
            )

        customers = Customer.objects.all()
        products = Product.objects.all()
        for _ in range(30):
            customer = random.choice(customers)
            order = Order.objects.create(customer=customer, total_price=0)
            num_products = random.randint(1, 5)
            selected_products = random.sample(list(products), num_products)
            for product in selected_products:
                quantity = random.randint(1, 10)
                order.products.add(product)
                order.total_price += product.price * quantity
                order.save()

        self.stdout.write('ok')
