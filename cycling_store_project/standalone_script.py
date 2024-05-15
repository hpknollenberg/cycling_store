import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "cycling_store_project.settings"
django.setup()

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELOW


from cycling_store_app.models import *

def customer():
    customer = Customer(name=input("Customer Name: "))
    customer.save()
    
def read_customers():
    customers = Customer.objects.all()
    for customer in customers:
        print(customer)

def update_customer():
    customer = Customer.objects.filter(name=input("Customer Name To Edit: ")).first()
    customer.name = input("Change Customer Name To: ")
    customer.save()

def delete_customer():
    Customer.objects.filter(name=input("Customer To Delete: ")).first().delete()



