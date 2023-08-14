def get_numbers_from_user():
    number1 = input("Enter the first number: ")
    number2 = input("Enter the second number: ")

    try:
        print(f"Your numbers is: {int(number1)} and {int(number2)}")
    except ValueError:
        print("You enter wrong value(-s)")


get_numbers_from_user()
