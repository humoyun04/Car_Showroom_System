from car_showroom import *

def main():
    #Creat object for class
    obj = Cars()

    # Using a methods
    print(obj.login(7))
    print(obj.choice_car())
    print(obj.choice_color())
    print(obj.contract())
    print(obj.deliveri())

if __name__ == "__main__":
    main()