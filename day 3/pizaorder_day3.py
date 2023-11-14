
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