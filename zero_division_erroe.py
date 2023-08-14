number1 = input("Enter the number 1: ")
number2 = input("Enter the number 2: ")

try:
    number1, number2 = int(number1), int(number2)
    result = number1/number2
    print(f"Result = {result}")
except ZeroDivisionError:
    if number2 == 0:
        print("The second number equal zero. Please enter another number")
