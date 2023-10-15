from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Пользователь {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=0)
    date = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photo/', blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    ORDER_TYPES = (
        ('active', 'активный'),
        ('complete', 'завершенный'),
        ('canceled', 'отмененный'),
    )
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(default='active', max_length=12, choices=ORDER_TYPES)

    def __str__(self):
        return f'Заказ {self.id}'
