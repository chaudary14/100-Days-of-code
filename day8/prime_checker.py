# def prime_checker(number):
#     is_prime = True
#     for i in range(2, int(number)):

#         if number % i == 0:
#             is_prime = False
    
#     if is_prime:
#         print("It's a prime number!")
#     else:
#         print("It's not a prime number!")

# n = int(input("enter number: "))
# prime_checker(number=n)


def prime_checker(number):
    is_prime= True
    for i in range(2, int(number)):
        x = number%i
        if x == 0:
            is_prime = False


    if is_prime:
        print("Prime Number")
    if is_prime== False:
        print("not Prime")
n = int(input("enter number: "))
prime_checker(number=n)

