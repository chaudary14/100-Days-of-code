import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list = [rock, paper, scissors]
option = int(input("What do you choose? Type '0' for rock, '1' for paper and '2' for scissor: \n Enter: "))
my_choice= (list[option])
print(my_choice)
print("Computer's choice")
com = random.choice(list)
print(com)

if my_choice == com:
    print("Draw")
elif my_choice == scissors and com == rock or my_choice == paper and com == scissors or my_choice == rock and com == paper:
    print("You lose")
else:
    print("You win")



