height = int(input("enter height in cm: "))
age = int(input("enter age: "))

if height >= 120:
    if age > 18:
       amount =  12
    elif age <= 18:
        amount = 7
    elif age < 12:
        amount = 5

    photo = input("do you want a photo? y or n: ")
    if photo == "y":
        total = int(amount) + 3
        print(f"Total amount is: ${total}")
    else:
        total = int(amount)
        print(f"Total amount is: ${total}")


else:
    print("you cannot ride")
