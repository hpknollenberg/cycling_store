from django.db import models

# Create your models here.

class Vehicle(models.Model):
    type = models.CharField(max_length = 10)
    number_in_stock = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    color = models.CharField(max_length=100)

    def __str__(self):
        return f'Vehicle Type: {self.type}'

class Customer(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return f'Customer Name: {self.name}'

class CustomerOrder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ManyToManyField(Vehicle)
    created_date = models.DateField()
    paid = models.BooleanField()

    def __str__(self):
        return f'{self.id}, {self.customer}, {self.order.first()}, {self.created_date}, Paid: {self.paid}'