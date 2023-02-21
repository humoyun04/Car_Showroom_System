from car_list import *
from delivery import *

class Cars:
    def __init__(self):
        pass

    def login(self,n:int):
        # Login Page
        print('''     ==== Welcome to the Online \"Car Showroom\"! ===
        Please go through registration first.''')
        # Catch errors
        try:
            name = input("Name: ")
            if len(name) == 0:
                return "Left a name!"
            lastname = input("Lastname: ")
            if len(lastname) == 0:
                return "Left a lastname!"
            pasport = int(input("Pasport ID: "))
            if len(str(pasport)) != n:
                return "Passport ID length must be 7 digits!"
        except ValueError:
            return "Login again!"

        # Write files
        with open("login.txt","w") as file:
            file.write(f"Inform Customers:\nName: {name},\nLastname: {lastname},\nPasport: {pasport}\n")

    def choice_car(self):
        # Choice the car
        print("  What type of car do you need:\n1.Sport Cars\n2.Cars")
        # Catch errors
        try:
            choice_car = int(input("Number type of the car: "))
            if len(str(choice_car)) == 0:
                return "Left a number type car!"
            if choice_car == 1:
                print("Write down the number of the car")
                sportCars()
            elif choice_car == 2:
                print("Write down the number of the car")
                Kars()
            else:
                return "Sorry,no such type!"

            car_number = int(input("Number of the Car: "))
            if len(str(car_number)) == 0:
                return "Left a number Car!"
        except ValueError:
            print("Login again!")
            return

        if choice_car == 1:
            car = sport_cars[car_number]
            for ind, val in enumerate(car):
                car_n = val[0]
                price_car_n = val[1]
            # Write files
            with open("login.txt","a") as file:
                file.write(f"\nInform for Product:\nCar: {car_n} : ${price_car_n}")
        elif choice_car == 2:
            kar = cars[car_number]
            for ind, val in enumerate(kar):
                kar_n = val[0]
                price_kar_n = val[1]
            # Write files
            with open("login.txt","a") as file:
                file.write(f"\nInform for Product:\nCar: {kar_n} : Price: ${price_kar_n}")

    def choice_color(self):
        # Choice color of the Car
        print("We have colors: ")
        Colors()
        color = int(input("Number of color: "))
        kolor = colors[color]
        for ind, val in enumerate(kolor):
            # Write files
            with open("login.txt", "a") as file:
                file.write(f"\nCar-color: {val}")

    def contract(self):

        #Contract Page
        # Read files
        with open("login.txt","r") as file:
            print(file.read())
        Contract = input("You agree to buy this product? Yes or Not: ")
        if Contract.lower() == "not":
            print("Ok you can choose Car again!")
            return
        else:
            pass
        print("How will you pay the amount you can pay online to our card")
        print("Pay now and get 10% discount\n \"Gold Cart: 3751 000000 98563\"\n \"Visa Cart: 4000 1234 5678 9010\" \n Thank You!")

    def deliveri(self):
        #Delivery Page
        print("Cities where we can deiliver the car ")
        delivery_city()
        city = input("Where to deliver your Car?: ")
        deliver(city)

        #Write files
        with open("login.txt", "a") as file:
            file.write(f"\nCar-delivery: {city}")












