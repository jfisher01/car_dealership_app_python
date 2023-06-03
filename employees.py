import fileinput

from inventory import Inventory
from sales import Sales

# employees class
class Employee:

    # Constructor for employees information
    def __init__(self,name,id_number,department,position):
        self.__name = name
        self.__id_number = id_number
        self.__department = department
        self.__position = position

    # Getters and setters for employee constructor
    def set_name(self):
        return self.__name

    def get_name(self):
        return self.__name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_id_number(self):
        return self.__id_number

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

    def set_position(self,position):
        self.__position = position

    def get_position(self):
        return self.__position

    # show hourly rate
    def show_hourly_pay_menu(self):
        print("Enter: \n1 for Managers\n2 for Supervisors\n3 for HR staff\n"
              + "4 for Maintenance\n5 for other staff\nEnter 0 to exit\n ")

    # view hourly pay rate
    def view_hourly_pay_rate(self):
        staff_pay = 8
        while not (0 < staff_pay <= 5):
            staff_pay += 1
            self.show_hourly_pay_menu()
            try:
                staff_pay = int(input("Select an option  "))
            except:
                print("Invalid entry")
                break
            if staff_pay == 1:
                hourly_pay_rate = 26
                print(f"Managers pay start from ${hourly_pay_rate:,.2f} per hour")
                print("You exited the program\n")
                break
            elif staff_pay == 2 :
                hourly_pay_rate = 23
                print(f"Supervisors pay start from ${hourly_pay_rate:,.2f} per hour")
                break
            elif staff_pay == 3 :
                hourly_pay_rate = 19
                print(f"HR Staff  pay is ${hourly_pay_rate:,.2f} per hour")
                break
            elif staff_pay == 4:
                hourly_pay_rate = 21
                print(f"Maintenance Technicians pay is ${hourly_pay_rate:,.2f} per hour")
                break
            elif staff_pay == 5:
                hourly_pay_rate = 18
                print(f"Other staff pay is ${hourly_pay_rate:,.2f} per hour")
                break
            else:
                print("Invalid entry")
                staff_pay = input("Enter 0 to exit ")
                break

        print("You exited the program\n")

    # Number of hours worked
    def numb_of_hours_worked(self):
        days_worked = float(input("Please enter number of days you worked?\n"))
        hours_worked = float(days_worked * 8)
        print(f"Number of hours worked is : {hours_worked} hours\n")

    # show employees menu
    def show_menu(self):
        print("*********************************")
        print("*     EMPLOYEES APP MANAGER     *")
        print("* Enter : \n" + "* 1 to get all staff information\n" + "* 2. to get a staff information\n"
                   + "* 3 to see hourly pay rate\n" + "* 4 to see number of hours worked" + "\n* 5 to see company's policy " + "\n* 6 to exit the program")
        print("**********************************\n")

    # String function for employees information
    def __str__(self):
        return f"Name: {self.__name }  \nID No: {self.__id_number} \nDept:  {self.__department}  \nPosition: {self.__position} \n"

    # Employee database
    def manage_staff(self):
        christian = Employee("Christian Wood", 102000, "IT ", "Administrator")
        kenny = Employee("Kenny Brook", 102001, "IT ", "Webmaster")
        marshal = Employee("Marshal Moore ", 102002, "IT ", "PC Technician")
        katlin = Employee("Katlin Kleene ", 102003, "HR ", "Manager")
        jack = Employee("Jack Jones ", 102004, "HR ", "Co-ordinator")
        heidi = Employee("Heidi Russel ", 102005, "HR ", "Co-ordinator")
        alicia = Employee("Alice Fox ", 102006, "HR ", "Payroll")
        peter = Employee("Peter Bell ", 102007, "Front Desk ", "Receptionis")
        charles = Employee("Charles Lee ", 102008, "Leasing ", "Leasing Specialist")
        ryan = Employee("Ryan Dove ", 102009, "Leasing ", "Leasing Specialist")
        garry = Employee("Garry Doon ", 102010, "Marketing ", "Marketing Officer")
        emy = Employee("Emy Hintz ", 102011, "Marketing ", "Marketing Officer")
        bruce = Employee("Bruce Madilan ", 102012, "Maintenance ", "Maintenance Manager")
        jake = Employee("Jake Busk ", 102013, "Maintenance ", "Maintenance Tech.")
        kerry = Employee("Kerry Pit ", 102014, "Maintenance ", "Maintenance Tech.")
        john = Employee("John Braswic ", 102015, "HR ", "Intern")

    # Dictionary datastructure for accessing employees information
        employee = {}
        employee.update({883: christian.__str__()})
        employee.update({555: kenny.__str__()})
        employee.update({567: marshal.__str__()})
        employee.update({457: katlin.__str__()})
        employee.update({135: jack.__str__()})
        employee.update({980: heidi.__str__()})
        employee.update({905: alicia.__str__()})
        employee.update({736: peter.__str__()})
        employee.update({102: charles.__str__()})
        employee.update({114: ryan.__str__()})
        employee.update({774: garry.__str__()})
        employee.update({806: emy.__str__()})
        employee.update({922: bruce.__str__()})
        employee.update({611: jake.__str__()})
        employee.update({541: kerry.__str__()})
        employee.update({117: john.__str__()})

        choice = 1
        ssn = 0
        while 0 < choice < 6:
            self.show_menu()
            try:
                choice = int(input("Enter an option\n "))
            except:
                print("Invalid entry")
                exit()
            if choice == 1:
                for x, y in employee.items():
                    print(x, y)
                break
            elif choice == 2:
                try:
                    ssn = int(input("Enter employee's last 3 ssn"))
                except:
                    print("Invalid entry")
                print(employee.get(ssn))

            elif choice == 3:
                self.view_hourly_pay_rate()
                break
            elif choice == 4:
                self.numb_of_hours_worked()
            elif choice == 5:
                company_policy = open('C:\\Users\\uchej\\PycharmProjects\\CarDealershipProject\\company_policy.txt','r')
                print(company_policy.read())
                fileinput.close()
                break
            else:
                print("invalid entry")
                break

        print("You exited the program")

    # Jack Duke Autosales Inc app manager central methods calls
    def launch_app(self):
        invoice = Sales('Honda','Accord',2019,4,5000,'VA334567P')

        employee1 = Employee("John", 89765, "Fabrication", "Manager")

        print("\nJACK DUKE AUTOSALES INC APP MANAGER\n"
              + " WE ARE SPECIALIST IN HONDA BRAND")
        print("**********************************")
        print(f"TO MANAGE EMPLOYEES, ENTER 1 \nTO MANAGE SALES, ENTER 2\nTO MANAGE INVENTORY ENTER 3 ")
        print("*********************************\n")

        select_task = ''
        try:
            select_task = int(input("Please select task "))
        except:
            print("Invalid entry")
            exit()
        if select_task == 1:
            employee1.manage_staff()
        elif select_task == 2:
            invoice.print_invoice()
        elif select_task == 3:
            Inventory.show_honda_menu()
            try:
                option = int(input("Please select an option\n "))
            except:
                print("Invalid entry")
                exit()
            if option == 1:
                Inventory.view_honda_model(Inventory.honda)
            elif option == 2:
                Inventory.view_all_model(Inventory.honda)
            elif option == 3:
                Inventory.update_year(Inventory.honda)
            elif option == 4:
                Inventory.update_status(Inventory.honda)
            elif option == 5:
                Inventory.update_mileage(Inventory.honda)
            elif option == 6:
                Inventory.update_color(Inventory.honda)
            elif option == 7:
                Inventory.update_quantity(Inventory.honda)
            elif option == 8:
                Inventory.update_price(Inventory.honda)
            elif option == 9:
                Inventory.update_all_info(Inventory.honda)
            else:
                print("Invalid entry or you exited ")
                exit()

        else:
            print("Invalid entry")
            exit()