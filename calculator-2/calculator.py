"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


while True:
    # get user input (should be an equation or q for quit command)
    print("Enter your equation (enter q to quit)")
    input_string = input("> ")

    tokens = input_string.split(' ')

    if len(tokens) == 1:
        if tokens[0].lower() == 'q':
            # if get the quit command, break out of the loop to end the program
            print("Calculator exiting")
            break
        elif tokens[0] == '':
            # if user doesn't enter anything, inform not enough input
            print("Not enough input")
            print()
        else:
            # if any other single token input other than q, inform not valid input
            print("Not valid input")
            print()
    elif len(tokens) == 2:
        try:
            # make sure the second token is a number
            num = float(tokens[1])

            if tokens[0].lower() == 'square':
                print(square(num))
            elif tokens[0].lower() == 'cube':
                print(cube(num))
            else:
                print("Not a valid equation")

            print()
        except ValueError:
            print("Please enter the operator you want first, then a number")
            print()
    elif len(tokens) == 3:
        try:
            num1 = float(tokens[1])
            num2 = float(tokens[2])

            if tokens[0] == '+':
                print(add(num1, num2))
            elif tokens[0] == '-':
                print(subtract(num1, num2))
            elif tokens[0] == '*':
                print(multiply(num1, num2))
            elif tokens[0] == "/":
                print(divide(num1, num2))
            elif tokens[0].lower() == 'pow' or tokens[0].lower() == 'power':
                print(power(num1, num2))
            elif tokens[0].lower() == "mod":
                print(mod(num1, num2))
            else:
                print("Not a valid equation")

            print()
        except ValueError:
            print("Please enter the operator you want first, then two numbers")
            print()
    else:
        print("Sorry, we can't handle that right now")
        print()