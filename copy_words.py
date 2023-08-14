file1 = open("file1_for_task7.txt", "a")
file2 = open("file2_for_task7.txt", "r")
content = file2.read()
# print(f"File 1 before editing: {file1.read()}")
print(file1.write(content))

file1.close()
file2.close()
