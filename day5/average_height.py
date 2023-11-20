height = input("Input a list of student's height: ").split(" ")

for n in range(0, len(height)):
    height[n] = int(height[n])

print(height)
    # sum = int(sum) + int(average)
# print(sum/len(height))
y = 0
sum = 0
for length in height:
    y = y + 1

for total in height:
    sum = int(sum) + int(total)
print(round(sum/y))
