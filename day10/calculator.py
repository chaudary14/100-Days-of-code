from calculator_art import logo
# print(logo)

#ADD FUNCTION 
def add(n1,n2):
    return n1 + n2

#substract FUNCTION 
def substract(n1,n2):
    return n1 - n2

#multiply FUNCTION 
def multiply(n1,n2):
    return n1 * n2

#divide FUNCTION 
def divide(n1,n2):
    return n1 / n2

operation = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide

}

# function = operation["+"]
# print(function(2,3))
def calculator():
    print(logo)
    num1 = float(input("Enter Number 1: "))
    for sign in operation:
        print(sign)

    continue_program = True
    while continue_program:

        operation_symbol = input("Pick Operation symbol: ")

        num2 = float(input("What's the next number: "))



        # Creating a variable function. and to access the value of the selected key in a dictionary we are using 
            # operation[operation_symbol] to acces the value of the selected operation by user in dictionary operation.
        function = operation[operation_symbol]
        # the value of operation dictionary has two arguments. e.g add function uses 2 arguments n1,n2. so we give two
        # to the varibale function. 
        answer = function(num1,num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        decision = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit! ")
        if decision == "n":
            continue_program = False
            calculator()
        if decision == "y":
            num1 = answer


calculator()