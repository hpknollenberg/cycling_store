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

def create_customer(): # This function grabs an input and assigns it to the customer name.
    customer = Customer(name=input("Customer Name: "))
    customer.save()
    return menu_func()
    
def read_customers(): # This function lists each of the customers.
    customers = Customer.objects.all()
    for customer in customers:
        print(customer)
    return menu_func()

def update_customer(): # This function allows the user to change a customer's name.
    try:
        customer = Customer.objects.filter(name=input("Customer Name To Edit: ")).first()
        customer.name = input("Change Customer Name To: ")
        customer.save()
        
    except:
        print("Customer Does Not Exist.")
    return menu_func()

def delete_customer(): # This function allows the user to delete a customer.
    try:
        Customer.objects.filter(name=input("Customer To Delete: ")).first().delete()
    except:
        print("Customer Does Not Exist.")
    return menu_func()



# VEHICLE

def create_vehicle(): # This function grabs an input of name and stock and assigns them to a new vehicle.
    try:
        vehicle = Vehicle(type=input("Type: "), number_in_stock=input("Stock: "), color=input("Color: "), price=input("Price: "))
        vehicle.save()
    except:
        print("Invalid Input.")
    return menu_func()
def read_vehicles(): # This function lists each vehicle type and stock.
    vehicles = Vehicle.objects.all()
    for vehicle in vehicles:
        print (vehicle, "Stock:", vehicle.number_in_stock, "Color:", vehicle.color, "Price:", vehicle.price)
    return menu_func()

def update_vehicle(): # This function allows the user to change the stock number of each vehicle.
    try:
        vehicle = Vehicle.objects.filter(type=input("Vehicle Type To Edit: "), color=input("Color: ")).first()
        vehicle.number_in_stock = int(input("Change Stock To: "))
        vehicle.save()
    except:
        print("Vehicle Does Not Exist.")
    return menu_func()

def delete_vehicle(): # This function allows the user to delete a vehicle.
    try:
        Vehicle.objects.filter(type=input("Vehicle To Delete: "), color=input("Color: ")).first().delete()
    except:
        print("Vehicle Does Not Exist In Inventory.")
    return menu_func()



# Customer Order

def create_customer_order(): # This function grabs inputs of vehicle, date, and customer name in order to create an order. It also subtracts from the corresponding vehicle's stock.

    customer_order = CustomerOrder(created_date=input("Order Date (YYYY-MM-DD): "), paid=False)
    try:
        customer_name = input("Customer Name: ")
        customer_order.customer = Customer.objects.get(name=customer_name)
        try:
            vehicle = Vehicle.objects.get(type=input("Vehicle Type: "), color=input("Color: "))
            customer_order.save()
            customer_order.order.add(vehicle)
            customer_order.save()
            try:
                vehicle.number_in_stock = vehicle.number_in_stock - 1
                vehicle.save()  
            except:
                print (f'{vehicle.type} Is Out Of Stock.')
        except:
            print("Unable To Locate Vehicle In System.")    
    except:
        print(f'Unable To Locate {customer_name} As A Customer.')
    return menu_func()

def read_customer_orders(): # This function lists each order.
    customer_orders = CustomerOrder.objects.all()
    for customer_order in customer_orders:
        print(f'{customer_order}')
    return menu_func()

def update_customer_order(): # This function allows the user to change an order's paid status.
    try:
        customer_order = CustomerOrder.objects.filter(id=input("Order ID: ")).first()
        paid_input = input("Change Paid To: ")
        if paid_input == "True":
            customer_order.paid = True
            customer_order.save()
        elif paid_input == "False":
            customer_order.paid = False
            customer_order.save()
        else:
            print("Invalid Input.")
    except: 
        print("Order Does Not Exist.")
    return menu_func()

def delete_customer_order(): # This function allows the user to delete an order. It also adds to the corresponding vehicle's stock.
    try:
        customer_order = CustomerOrder.objects.filter(id=input("Order ID: ")).first()
        
        try:
            vehicle = Vehicle.objects.get(type=customer_order.order.first().type)
            vehicle.number_in_stock = vehicle.number_in_stock + 1
            vehicle.save()
        except:
            pass
        
        CustomerOrder.objects.filter(id=customer_order.id).first().delete()
    except:
        print("Order Does Not Exist.")
    return menu_func()

def read_specific_customer_orders():
    try:
        customer_orders = CustomerOrder.objects.filter(customer=Customer.objects.get(name=input("Customer Name: "))).all()
        for customer_order in customer_orders:
            print(f'{customer_order}')
    except:
        print ("Customer Does Not Exist.")
    return menu_func()


    
# MENU

def menu_func():
    
    firstOptionSelect = input("***** \n1:Customer Info \n2:Vehicle Info \n3:Order Info \n4:Quit \n***** \n")


    if firstOptionSelect == "1":
        optionSelectCustomer = input("***** \n1:Create New Customer \n2:List Customers \n3:Edit Customer \n4:Delete Customer \n5:Customer Order History \n6:Quit \n***** \n")

        if optionSelectCustomer == "1":
            return create_customer()
        elif optionSelectCustomer == "2":
            return read_customers()
        elif optionSelectCustomer == "3":
            return update_customer()
        elif optionSelectCustomer == "4":
            return delete_customer()
        elif optionSelectCustomer == "5":
            return read_specific_customer_orders()
        elif optionSelectCustomer == "6":
            pass
        else:
            print("Please Enter A Valid Input.")
            return menu_func()

    elif firstOptionSelect == "2":
        optionSelectVehicle = input("***** \n1:Add Vehicle \n2:Inventory of Vehicles \n3:Update Vehicle \n4:Delete Vehicle \n5:Quit \n***** \n")

        if optionSelectVehicle == "1":
            return create_vehicle()
        elif optionSelectVehicle == "2":
            return read_vehicles()
        elif optionSelectVehicle == "3":
            return update_vehicle()
        elif optionSelectVehicle == "4":
            return delete_vehicle()
        elif optionSelectVehicle == "5":
            pass
        else:
            print("Please Enter A Valid Input.")
            return menu_func()

    elif firstOptionSelect == "3":
        optionSelectOrder = input("***** \n1:Create Order \n2:List Orders \n3:Update Order \n4:Delete Order \n5:Quit \n***** \n")

        if optionSelectOrder == "1":
            return create_customer_order()
        elif optionSelectOrder == "2":
            return read_customer_orders()
        elif optionSelectOrder == "3":
            return update_customer_order()
        elif optionSelectOrder == "4":
            return delete_customer_order()
        elif optionSelectOrder == "5":
            pass
        else:
            print("Please Enter A Valid Input.")
            return menu_func()
    
    elif firstOptionSelect == "4":
        pass

    else:
        print("Please Enter A Valid Input.")
        return menu_func()

menu_func()

print("*********************************************")
print("*********************************************")
print("*******__***************| |******************")
print("***** /  '  __   __   __| |__        __ *****")
print("*****|  _  |  | |  | |  | |  | \\  / /__|*****")
print("***** \\__| |__| |__| |__| |__|  \\/  \\__ *****")
print("*****                           /       *****")
print("*******************************/*************")
print("*********************************************")
print("*********************************************")