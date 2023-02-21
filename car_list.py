sport_cars = {
    1: [("Porsche 911",320000)],
    2: [("Porsche 718 Cayman GTS 4.0",360000)],
    3: [("Chevrolet Corvette C8",290000)],
    4: [("Alpine A110 R",350000)],
    5: [("Jaguar F-Type",240000)],
    6: [("Mersedes-AMG GT",380000)],
    7: [("Audi TT RS",400000)],
    8: [("Lexus LC",410000)],
}

cars = {
    1: [("Mercedes-Benz AMG G 63",220000)],
    2: [("Kia Seltos",80000)],
    3: [("Honda Jazz",140000)],
    4: [("Nissan Magnite",190000)],
    5: [("Toyoto Land Cruiser 300",110000)],
    6: [("Scoda Octavia",90000)],
    7: [("Mercedes-Benz E-Class",245000)],
    8: [("Mercedes-Benz Maybach",300000)]
}

colors = {
    1: ["Opulent Blue"],
    2: ["Silver Coast"],
    3: ["Glacier Blue"],
    4: ["Mocha Steel"],
    5: ["Radiant Silver"],
    6: ["Sapphire Blue"],
    7: ["Black Ice"],
    8: ["Blue Flame"],
    9: ["Tuxedo Black"],
    10: ["Blue Jeans"],
    11: ["Green Envy"],
    12: ["Green Envy"],
    13: ["White"]
}

def sportCars():
    for num,val in sport_cars.items():
        print(f"{num}:")
        for ind,name in enumerate(val):
            print(f"  {name[0]} : ${name[1]},")


def Kars():
    for num,val in cars.items():
        print(f"{num}:")
        for ind,name in enumerate(val):
            print(f"  {name[0]} : ${name[1]},")

def Colors():
    for num,val in colors.items():
        print(f"{num}: {val[0]},")

