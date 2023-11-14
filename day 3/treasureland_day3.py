print("WELCOME TO TREAUSRE LAND!")
print("YOUR MISSION IS TO TO FIND THE TREASURE")
inp = input("You are at cross road.where do you want to go? TYPE left OR right\n").lower()

if inp == "left":
    ch = input("You came to lake. you want to wait or swim? Type \"wait\" OR \"swim\"\n")
    if ch == "wait":
        door =input("You arrive at island unharmed. there are 3 doors. Which door? TYPE blue, red OR yellow?")
        if door == "yellow":
            print("YOu found the treasure! YOU WIN!")
        else:
            print("GAME OVER")
    else:
        print("You got attacked by angry trout! GAME OVER")
else:
    print("You fell into a hole! GAME OVER")