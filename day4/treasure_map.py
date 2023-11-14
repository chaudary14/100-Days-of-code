row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]


map = [row1 , row2, row3]
print(f"{row1}\n{row2}\n{row3}\n")



place = input("Where do you want to put the treasure? ")
horizontal, vertical  = place[0], place[1]

column= int(horizontal) - 1
row = int(vertical) - 1

map[row][column] = "x"
# or 
#selected_row = map[row]
#selected_row[column] = "x" 

print(f"{row1}\n{row2}\n{row3}\n")

