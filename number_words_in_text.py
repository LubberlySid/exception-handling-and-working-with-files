file = open("file_for_count_words", "r")
content = file.read()
words = content.split()
print(f"Number of words in this file is: {len(words)}")
