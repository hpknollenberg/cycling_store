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

# CUSTOMER

def create_customer():
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



# VEHICLE

# def create_vehicle():
#     vehicle = Vehicle(type=input("Type: "), number_in_stock=input("Stock: "))
#     vehicle.save()

def read_vehicles():
     vehicles = Vehicle.objects.all()
     for vehicle in vehicles:
         print (vehicle, "Stock:", vehicle.number_in_stock)

def update_vehicle():
    vehicle = Vehicle.objects.filter(type=input("Vehicle Type To Edit: ")).first()
    vehicle.number_in_stock = int(input("Change Stock To: "))
    vehicle.save()

# def delete_vehicle():
#     Vehicle.objects.filter(type=input("Vehicle To Delete: ")).first().delete()



# Customer Order

def create_customer_order():
    customer_order = CustomerOrder(created_date=input("Order Date (YYYY-MM-DD): "), paid=False)
    customer_order.customer = Customer.objects.get(name=input("Customer Name: "))
    customer_order.save()

    vehicle = Vehicle.objects.get(type=input("Vehicle Type: "))
    customer_order.order.add(vehicle)
    customer_order.save()
    
    vehicle.number_in_stock = vehicle.number_in_stock - 1
    vehicle.save()

def read_customer_orders():
    customer_orders = CustomerOrder.objects.all()
    for customer_order in customer_orders:
        print(f'{customer_order}')

def update_customer_order():
    customer_order = CustomerOrder.objects.filter(created_date=input("Date Of Order To Update: "), customer=Customer.objects.get(name=input("Customer Of Order To Update: "))).first()
    customer_order.paid = input("Change Paid To: ")

def delete_customer_order():
    delete_date = input("Date Of Order To Delete: ")
    delete_customer = input("Customer Of Order To Delete: ")
    customer_order = CustomerOrder.objects.filter(created_date=delete_date, customer=Customer.objects.get(name=delete_customer)).first()
    
    vehicle = Vehicle.objects.get(type=customer_order.order.first().type)
    vehicle.number_in_stock = vehicle.number_in_stock + 1
    vehicle.save()
    
    CustomerOrder.objects.filter(created_date=delete_date, customer=Customer.objects.get(name=delete_customer)).first().delete()
    

    
    


# create_vehicle()
# read_vehicles()


# create_customer()
# read_customers()

# create_customer_order()
# read_customer_orders()
# delete_customer_order()

# read_vehicles()
# delete_vehicle()

optionSelect = input("1:Create New Customer \n2:Create Order \n3:Cancel Order \n4:Edit Order \n5:Inventory \n6:Order More Vehicles \n")

if optionSelect == "1":
    create_customer()
if optionSelect == "2":
    create_customer_order()
if optionSelect == "3":
    delete_customer_order()
if optionSelect == "4":
    update_customer_order()
if optionSelect == "5":
    read_vehicles()
if optionSelect == "6":
    update_vehicle()
else:
    print("Please choose 1-6.")