try:
    file = open("NE.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    file = open("new.txt", "r")
    print(f"File NE.txt was not found, so read file new.txt:\n{file.read()}")
    file.close()
