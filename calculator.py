"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    user_input = input("> ")
    tokens = user_input.split(" ")
    
    if tokens[0] == "q":
        print("Thanks for using our calculator")
        break
    else:
        num1 = float(tokens[1])
        try:
            num2 = float(tokens[2])
        except: 
            num2 = 0
        if tokens[0] == "+":
            print(add(num1, num2))
        elif tokens[0] == "-":
            print(subtract(num1, num2))
        elif tokens[0] == "*":
            print(multiply(num1, num2))
        elif tokens[0] == "/":
            print(divide(num1, num2))
        elif tokens[0] == "square":
            print(square(num1))
        elif tokens[0] == "cube":
            print(cube(num1))
        elif tokens[0] == "pow":
            print(power(num1, num2))
        elif tokens[0] == "mod":
            print(mod(num1, num2))

            

# Replace this with your code
