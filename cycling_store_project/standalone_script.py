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
    return menu_func()
    
def read_customers():
    customers = Customer.objects.all()
    for customer in customers:
        print(customer)
    return menu_func()

def update_customer():
    try:
        customer = Customer.objects.filter(name=input("Customer Name To Edit: ")).first()
        customer.name = input("Change Customer Name To: ")
        customer.save()
        
    except:
        print("Customer Does Not Exist.")
    return menu_func()

def delete_customer():
    try:
        Customer.objects.filter(name=input("Customer To Delete: ")).first().delete()
    except:
        print("Customer Does Not Exist.")
    return menu_func()



# VEHICLE

def create_vehicle():
    vehicle = Vehicle(type=input("Type: "), number_in_stock=input("Stock: "))
    vehicle.save()
    return menu_func()

def read_vehicles():
    vehicles = Vehicle.objects.all()
    for vehicle in vehicles:
        print (vehicle, "Stock:", vehicle.number_in_stock)
    return menu_func()

def update_vehicle():
    try:
        vehicle = Vehicle.objects.filter(type=input("Vehicle Type To Edit: ")).first()
        vehicle.number_in_stock = int(input("Change Stock To: "))
        vehicle.save()
    except:
        print("Vehicle Does Not Exist.")
    return menu_func()

def delete_vehicle():
    try:
        Vehicle.objects.filter(type=input("Vehicle To Delete: ")).first().delete()
    except:
        print("Vehicle Does Not Exist In Inventory.")
    return menu_func()



# Customer Order

def create_customer_order():
    
    vehicle = Vehicle.objects.get(type=input("Vehicle Type: "))
    
    if (vehicle.number_in_stock > 0):
        customer_order = CustomerOrder(created_date=input("Order Date (YYYY-MM-DD): "), paid=False)
        try:
            customer_name = input("Customer Name: ")
            customer_order.customer = Customer.objects.get(name=customer_name)
            customer_order.save()

            customer_order.order.add(vehicle)
            customer_order.save()
            
            vehicle.number_in_stock = vehicle.number_in_stock - 1
            vehicle.save()
        except:
            print(f'Unable To Locate {customer_name} As A Customer.')
            
    else:
        print (f'{vehicle.type} Is Out Of Stock.')
    return menu_func()

def read_customer_orders():
    customer_orders = CustomerOrder.objects.all()
    for customer_order in customer_orders:
        print(f'{customer_order}')
    return menu_func()

def update_customer_order():
    try:
        customer_order = CustomerOrder.objects.filter(created_date=input("Date Of Order To Update: "), customer=Customer.objects.get(name=input("Customer Of Order To Update: "))).first()
        paid_input = input("Change Paid To: ")
        if paid_input == "True":
            customer_order.paid = True
            customer_order.save()
        elif paid_input == "False":
            customer_order.paid = False
            customer_order.save()
    except: 
        print("Order Does Not Exist.")
    return menu_func()

def delete_customer_order():
    try:
        delete_date = input("Date Of Order To Delete: ")
        delete_customer = input("Customer Of Order To Delete: ")
        customer_order = CustomerOrder.objects.filter(created_date=delete_date, customer=Customer.objects.get(name=delete_customer)).first()
        
        vehicle = Vehicle.objects.get(type=customer_order.order.first().type)
        vehicle.number_in_stock = vehicle.number_in_stock + 1
        vehicle.save()
        
        CustomerOrder.objects.filter(created_date=delete_date, customer=Customer.objects.get(name=delete_customer)).first().delete()
    except:
        print("Order Does Not Exist.")
    return menu_func()

    
    

def menu_func():
    optionSelect = input("***** \n1:Create New Customer \n2:List Customers \n3:Edit Customer \n4:Delete Customer \n5:Create Order \n6:List Orders \n7:Update Order \n8:Delete Order \n9:Add Vehicle \n10:Inventory of Vehicles \n11:Update Vehicle \n12:Delete Vehicle \n13:Quit \n***** \n")
    
    if optionSelect == "1":
        return create_customer()
    if optionSelect == "2":
        return read_customers()
    if optionSelect == "3":
        return update_customer()
    if optionSelect == "4":
        return delete_customer()
    if optionSelect == "5":
        return create_customer_order()
    if optionSelect == "6":
        return read_customer_orders()
    if optionSelect == "7":
        return update_customer_order()
    if optionSelect == "8":
        return delete_customer_order()
    if optionSelect == "9":
        return create_vehicle()
    if optionSelect == "10":
        return read_vehicles()
    if optionSelect == "11":
        return update_vehicle()
    if optionSelect == "12":
        return delete_vehicle()
    if optionSelect == "13":
        pass
    else:
        print("Please Enter 1-13.")

menu_func()


This is the newfunction branch.