letters = 0
text = input("Write your text here: ")

for char in text:
    if char != " ":
        letters += 1

print(f"Your text has {letters} letters.")
