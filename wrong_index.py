data = ["John", 15, "student"]

try:
    print(data[3])
except IndexError:
    print("You enter wrong index")
