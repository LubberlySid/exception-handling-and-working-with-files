file = open("file_to modify_task9", "r")
file1 = open("file_to modify_task9", "r+")
lines = file.readlines()
line_to_remove = "Today is sunny"
file1.seek(0)

for line in lines:
    if line.strip() != line_to_remove:
        file1.write(line)

file1.truncate()
file1.seek(0)

print(file1.read())
file.close()
file1.close()
