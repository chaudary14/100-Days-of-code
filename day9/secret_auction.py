import sys, subprocess
import hammer_art
print(hammer_art.logo)
print("WELCOME TO THE SECRET AUCTION PROGRAM!")
dictionary = {}
continu = True
while continu:
    name= input("What is your name? ")
    bid = int(input("What's your bid? $"))
    dictionary[name] = bid
    repeat= input("Are there any other bidders? 'Yes' or 'No': ").lower()
    if repeat != "yes":
        continu = False
    else:
        subprocess.run("cls",shell=True)

# print(dictionary)
high = 0
for large in dictionary:
    if dictionary[large] > high:
        high = dictionary[large]
        final = f"The Winner is {large} with bid of ${high}"
subprocess.run("cls",shell=True)
print(final)
