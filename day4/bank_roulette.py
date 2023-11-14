import random
name_string = input("Give me everybody's name, separated by a comma ")
names = name_string.split(", ")
# easy method is to use random.choice(names)

# print(names[0].title())

length = len(names)
x = random.randint(0,length-1)


h = names[x]
print(h.title(),"is going to pay")

# print(f"{names[y]} is going to pay the bill.")

