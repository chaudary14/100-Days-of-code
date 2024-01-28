# Round up a number = ceil() method, round down a number floor()
# The ceil() function gets its name from the mathematical term ceiling, 
# which describes the nearest integer that's greater than or equal to a given number.
from math import ceil, floor

def paint_area(height, width, coverage):
    number_of_cans = (int(height) * int(width)) / int(coverage)
    print("you'll need ", ceil(number_of_cans), "cans of paint. ")


x = input("Height: ")
y= input("Width: ")
cover = 5

paint_area(height=x, width=y,coverage= cover )
