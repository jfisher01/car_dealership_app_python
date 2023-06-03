
class Inventory:
    # Honda inventroy database
    honda = {
        "ACCORD": {
            "name": "ACCORD",
            "year": 2015,
            "status": "used",
            "mileage": 34000,
            "color": "white",
            "quantity": 4,
            "price": 25000,
        },
        "CR-V": {
            "name": "CR-V",
            "year": 2023,
            "status": "new",
            "mileage": 0,
            "color": "blue",
            "quantity": 3,
            "price": 29000,
        },
        "PILOT": {
            "name": "PILOT",
            "year": 2020,
            "status": "used",
            "mileage": 10000,
            "color": "ash",
            "quantity": 3,
            "price": 18000,
        },
        "PASSPORT": {
            "name": "PASSPORT",
            "year": 2016,
            "status": "used",
            "mileage": 50000,
            "color": "milk",
            "quantity": 5,
            "price": 13000,
        },
        "CROSSTOUR": {
            "name": "CROSSTOUR",
            "year": 2022,
            "status": "new",
            "mileage": 0,
            "color": "metalic",
            "quantity": 3,
            "price": 22000,
        },
        "ELITE": {
            "name": "ELITE",
            "year": 2023,
            "status": "new",
            "mileage": 0,
            "color": "blue",
            "quantity": 6,
            "price": 25000,
        },
        "RIDGELINE": {
            "name": "RIDGELINE",
            "year": 2023,
            "status": "new",
            "mileage": 0,
            "color": "blue",
            "quantity": 3,
            "price": 26000,
        },
        "ODYSSEY": {
            "name": "ODYSSEY",
            "year": 2021,
            "status": "used",
            "mileage": 15000,
            "color": "blue",
            "quantity": 7,
            "price": 20000,
        },
        "HR-V": {
            "name": "HR-V",
            "year": 2019,
            "status": "used",
            "mileage": 29000,
            "color": "blue",
            "quantity": 7,
            "price": 19000,
        }
    }

    #print_update()

    # View a honda model
    def view_honda_model(d):
        choice = input("Enter a Honda model ").upper()
        for model, model_info in d.items():
            if choice in model:
                print("\nHONDA MODEL:", model)
                for key in model_info:
                    print(key + ':', model_info[key])
        else:
            print("Not in our inventory")

    # View all Honda models
    def view_all_model(d):
        for model, all_model_info in d.items():
            print("\nHONDA MODEL:", model)
            for key in all_model_info:
                print(key + ':', all_model_info[key])

    # Update Honda model's year
    def update_year(d):
        choice = ''
        try:
            choice = input("Enter Honda model to edit year ").upper()
        except:
            print("Invalid entry")
        try:
            new_year = int(input("Enter new year "))
            d[choice]["year"] = new_year
        except:
            print("Invalid entry")
        for model, model_info in d.items():
            if choice in model:
                print("\nHONDA MODEL:", model)
                for key in model_info:
                    print(key + ':', model_info[key])

    # Update Honda model's status
    def update_status(d):
        choice = ''
        try:
            choice = input("Enter Honda model to edit status ").upper()
        except:
            print("Invalid entry")
        try:
            new_status = input("Enter new status ")
            d[choice]["status"] = new_status
        except:
            print("Invalid entry")
        for model, model_info in d.items():
            if choice in model:
                print("\nHONDA MODEL:", model)
                for key in model_info:
                    print(key + ':', model_info[key])

    # Update Honda model's mileage
    def update_mileage(d):
        choice = ''
        try:
            choice = input("Enter Honda model to edit mileage ").upper()
        except:
            print("Invalid entry")
        try:
            new_mileage = int(input("Enter new mileage "))
            d[choice]["mileage"] = new_mileage
        except:
            print("Invalid entry")
        for model, model_info in d.items():
            if choice in model:
                print("\nHONDA MODEL:", model)
                for key in model_info:
                    print(key + ':', model_info[key])

    # Update Honda model's color
    def update_color(d):
        choice = ''
        try:
            choice = input("Enter Honda model to edit color ").upper()
        except:
            print("Invalid entry")
        try:
            new_color = input("Enter new color ")
            d[choice]["color"] = new_color
        except:
            print("Invalid entry")
        for model, model_info in d.items():
            if choice in model:
                print("\nHONDA MODEL:", model)
                for key in model_info:
                    print(key + ':', model_info[key])

    # Update Honda model's quantity in the inventory
    def update_quantity(d):
        choice = ''
        try:
            choice = input("Enter Honda model to edit quantity ").upper()
        except:
            print("Invalid entry")
        try:
            new_quantity = int(input("Enter new quantity "))
            d[choice]["quantity"] = new_quantity
        except:
            print("Invalid entry")
        for model, model_info in d.items():
            if choice in model:
                print("\nHONDA MODEL:", model)
                for key in model_info:
                    print(key + ':', model_info[key])

    # Update Honda model's current price
    def update_price(d):
        choice = ''
        try:
            choice = input("Enter Honda model to edit price ").upper()
        except:
            print("Invalid entry")
        try:
            new_price = int(input("Enter new price "))
            d[choice]["price"] = new_price
        except:
            print("Invalid entry")
        for model, model_info in d.items():
            if choice in model:
                print("\nHONDA MODEL:", model)
                for key in model_info:
                    print(key + ':', model_info[key])

    # Update all information for a selected Honda model
    def update_all_info(d):
        choice = ''
        try:
            choice = input("Enter Honda model to edit all info ").upper()
        except:
            print("Invalid entry")
        try:
            new_year = int(input("Enter new year "))
            d[choice]["year"] = new_year
        except:
            print("Invalid entry")
        try:
            new_status = input("Enter new status ")
            d[choice]["status"] = new_status
        except:
            print("Invalid entry")
        try:
            new_mileage = int(input("Enter new mileage "))
            d[choice]["mileage"] = new_mileage
        except:
            print("Invalid entry")
        try:
            new_color = input("Enter new color ")
            d[choice]["color"] = new_color
        except:
            print("Invalid entry")
        try:
            new_quantity = int(input("Enter new quantity "))
            d[choice]["quantity"] = new_quantity
        except:
            print("Invalid entry")
        try:
            new_price = int(input("Enter new price "))
            d[choice]["price"] = new_price
        except:
            print("Invalid entry")
        for model, model_info in d.items():
            if choice in model:
                print("\nHONDA MODEL:", model)
                for key in model_info:
                    print(key + ':', model_info[key])

    # View Honda inventory menu
    def show_honda_menu():
        menu = "\nEnter 1 to view a honda model\n"\
               + "2 to view all models and all model information\n"\
               + "3 to update model's year\n" + "4 to update model's status\n"\
               + "5 to update model's mileage\n" + "6 to update model's color\n"\
               + "7 to update model's quantity\n" + "8 to update model's price\n"\
               + "9 to update model's all information\n" + "10 to exit\n"
        print(menu)

