for x in range(1,101):
    if x%3 == 0 and x%5 == 0:
        print("FIZZ BUZZ")
    elif x%3 == 0:
        print("FIZZ")
    elif x%5 == 0:
        print("BUZZ")
    else:
        print(x)