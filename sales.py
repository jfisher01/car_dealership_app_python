
from inventory import Inventory
from datetime import date
import random

# Get current date
today = date.today()

# Create Invoice class
class Sales:
    # Constructor for Invoice class
    def __init__(self, make, model, year, quantity, price, vin):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__quantity = quantity
        self.__price = price
        self.__vin = vin

    # Setter for car make
    def set_make(self, make):
        self.__make = make

    # Setter for car model
    def set_model(self, model):
        set.__model = model

    # Setter for car year
    def set_year(self, year):
        set.__year = year

    # Setter for car quantity
    def set_quantity(self, quantity):
        set.__quantity = quantity

    # Setter for car price
    def set_price(self, price):
        set.__price = price

    # Setter for vehicle's number
    def set_vin(self, vin):
        set.__vin = vin

    # Getter for car make
    def get_make(self):
        self.__make = str(input('Please enter "honda" for make: ')).lower()
        if self.__make == 'honda':
            return self.__make
        else:
            print("Invalid entry")
            exit()

    # Getter for car model
    def get_model(self):
        self.__model = str(input('Please enter model: '))
        return self.__model

    # Getter for car year
    def get_year(self):
        self.__year  = int(input('Please enter year: '))
        return self.__year

    # Getter for car quantity
    def get_quantity(self):
        self.__quantity = int(input('Please enter quantity:'))
        if self.__quantity >= 0:
            return int(self.__quantity)
        else:
            return 'Quantity cannot be less than 0'

    # Getter for car price
    def get_price(self):
        self.__price = float(input('Please enter price:'))
        if self.__price >= 0:
            f'{self.__price:,.2f}'
            return self.__price
        else:
            return ' Price cannot be less than 0'

    # Getter for car Vehicle's identification number
    def get_vin(self):
        self.__vin = str(input('Please enter vehicle identification number: '))
        return self.__vin

    # String method to get print all car's information
    def __string__(self):
        return f'\nMake: {self.get_make()} \nModel: {self.get_model()}\nYear: {self.get_year()}\nQuantity : {self.get_quantity()}\nPrice: ${self.get_price()}\nVehicle Id Number : {self.get_vin()} '

    # Print invoice
    def print_invoice(self):
        make = self.get_make()

        model = self.get_model()

        year = self.get_year()

        quantity = self.get_quantity()

        price = self.get_price()

        vehicle_id_number = self.get_vin()

        invoice = {'Make': [], 'Model': [], 'Year': [], 'Quantity': [],'Price': [], 'VehicleId': []}

        invoice['Make'].append(make)
        invoice['Model'].append(model)
        invoice['Year'].append(year)
        invoice['Quantity'].append(quantity)
        invoice['Price'].append(price)
        invoice['VehicleId'].append(vehicle_id_number)

        invoice = {
            "Make": make,
            "Model": model,
            "Year": year,
            "Quantity": quantity,
            "Price": price,
            "Vehicle Id Number": vehicle_id_number
        }
        print('\n*************************************************')
        print('JACK DUKE AUTOSALES INC.', '    DATE: ',today, '\n*************************************************\n')
        print('    RECEIPT OF PAYMENT','    RECEIPT #:',self.receipt_no())
        for x, y in invoice.items():

            print(x, ': ', y)

        invoice_amount = self.__price * self.__quantity

        if invoice_amount >= 0:
            print(f'\nPrice = ${invoice_amount:,.2f}', '\n*************************************************')
        else:
            print('?\nInvoice amount must be equal or greater than 0')

    # Get receipt number
    @staticmethod
    def receipt_no():
        num = random.randint(10002,20000)
        num += num
        return int(num)
