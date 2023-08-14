file1 = open("file1_task8.txt", "r")
file2 = open("file2_task8.txt", "r")

content1 = set(file1.readlines())
content2 = set(file2.readlines())
unique_lines = [line for line in content1 if line not in content2]

for line in unique_lines:
    print(line.strip())

file1.close()
file2.close()
