numbers = input("Input student's numbers: ").split(" ")

for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])
print(numbers)
y = 0
 
for high in numbers:
    if high > y:
        y = high
print(f"The highest score in the class is: {y}")