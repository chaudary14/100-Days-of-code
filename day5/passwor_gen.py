import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



print("WELCOME TO PASSWORD GENERATOR! ")
letter_coun = int(input("How many letters would you like in your password? \n"))
symbols_coun = int(input("How many symbols would you like in your password? \n"))
numbers_coun = int(input("How many numbers would you like in your password? \n"))
password = []
# print("\nHERE IS YOUR PASSWORD: ", end=(""))
for x in range(letter_coun):
    y = random.choice(letters)
    
    password += y
# print(password)
for x in range(symbols_coun):
    y = random.choice(symbols)

    password += y

for x in range(numbers_coun):
    y = random.choice(numbers)

    password += y

print(password)
# h =print(random.shuffle(password))
# k = (random.shuffle(h))
k =random.shuffle(password)
print(password)
print("\nHERE IS YOUR PASSWORD: ", end=(""))

for h in password:
    print(h, end=(""))