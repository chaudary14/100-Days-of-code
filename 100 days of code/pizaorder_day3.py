"""
large = 25
medium = 20
small = 15
peper_large = 3
peper_small = 2
chess = 1

print("WELCOME TO PYTHON PIZZA DELIVERIES!")

size = input("which pizza size do you want? L , M or S: ")

pepronii = input("do you want to add extra peperonni? Y or N: ")
cheese = input("Extra Cheese? Y or N: ")

bill = 0

if size == "l":
    if pepronii == "y":
        if cheese == "y":
            total = large + peper_large + chess
            print(f"your final bill is: ${total}")
        else:
            total = large + peper_large
            print(f"your final bill is: ${total}")
    else:
        total = large
        print(f"your final bill is: ${total}")
elif size == "m":
    if pepronii == "y":
        if cheese == "y":
            total = medium + peper_large + chess
            print(f"your final bill is: ${total}")
        else:
            total = medium + peper_large
            print(f"your final bill is: ${total}")
    else:
        total = medium
        print(f"your final bill is: ${total}")
else:
    if pepronii == "y":
        if cheese == "y":
            total = small + peper_small + chess
            print(f"your final bill is: ${total}")
        else:
            total = small + peper_small
            print(f"your final bill is: ${total}")
    else:
        total = small
        print(f"your final bill is: ${total}")
"""
print("WELCOME TO PYTHON PIZZA DELIVERIES!")

size = input("which pizza size do you want? L , M or S: ")

pepronii = input("do you want to add extra peperonni? Y or N: ")
cheese = input("Extra Cheese? Y or N: ")

bill = 0


if size == "l":
    bill += 25
elif size == "m":
    bill += 20
else:
    bill += 15


if pepronii == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
    

if cheese == "y":
    bill += 1


print(f"YOur final bill is ${bill}")