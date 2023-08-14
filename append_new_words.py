filename = "text_for_append_new_words.txt"
file = open(filename, "w+")
print(f"File before editing: {file.read()}")
file.write("Today is hot")
file.seek(0)
print(f"File after editing: {file.read()}")

file.close()
