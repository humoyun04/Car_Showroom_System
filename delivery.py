cities = {
    "New York": 778,
    "Los Angeles": 1216,
    "Chicago": 589,
    "Houston": 1658,
    "Phoenix": 1341,
    "Philadephia": 348,
    "San Antonio": 1291,
    "Sam Diego": 844,
    "Dallas": 879,
    "San Jose": 461,
}

def deliver(city):
    shipping = 200
    try:
        if cities[city] <= 348:
            print(f"Shipping cost from you: ${shipping}\nThank You")
            return True
        elif cities[city] <= 461:
            shipping += 100
            print(f"Shipping cost from you: ${shipping}\nThank You")
            return True
        elif cities[city] <= 589:
            shipping += 150
            print(f"Shipping cost from you: ${shipping}\nThank You")
            return True
        elif cities[city] <= 778:
            shipping += 200
            print(f"Shipping cost from you: ${shipping}\nThank You")
            return True
        elif cities[city] <= 844:
            shipping += 300
            print(f"Shipping cost from you: ${shipping}\nThank You")
            return True
        elif cities[city] <= 879:
            shipping += 400
            print(f"Shipping cost from you: ${shipping}\nThank You")
            return True
        elif cities[city] <= 1216:
            shipping += 450
            print(f"Shipping cost from you: ${shipping}\nThank You")
            return True
        elif cities[city] <= 1291:
            shipping += 500
            print(f"Shipping cost from you: ${shipping}\nThank You")
            return True
        elif cities[city] <= 1341:
            shipping += 600
            print(f"Shipping cost from you: ${shipping}\nThank You")
            return True
        elif cities[city] <= 1658:
            shipping += 700
            print(f"Shipping cost from you: ${shipping}\nThank You")
            return True
    except KeyError:
        print(f"Dear customer, we can't temporarily deliver to such a long distance...\nWe will definitely start delivering to {city} soon!")
        return False

def delivery_city():
    for ind,val in cities.items():
        print(ind)

