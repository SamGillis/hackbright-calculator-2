"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    user_input = input("> ")
    tokens = user_input.split(" ")
    numbers = []
    for each in tokens[1:]:
        each = float(each)
        numbers.append(each)   

    if tokens[0] == "q":
        print("Thanks for using our calculator")
        break
    else:
        if tokens[0] == "+":
            print(add(numbers))
        elif tokens[0] == "-":
            print(subtract(numbers))
        elif tokens[0] == "*":
            print(multiply(numbers))
        elif tokens[0] == "/":
            print(divide(numbers))
        elif tokens[0] == "square":
            print(square(numbers))
        elif tokens[0] == "cube":
            print(cube(numbers))
        elif tokens[0] == "pow":
            print(power(numbers))
        elif tokens[0] == "mod":
            print(mod(numbers))

            

# Replace this with your code
