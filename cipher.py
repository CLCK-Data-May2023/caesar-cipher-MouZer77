import string

text = input("Please Enter Sentence to Be Encrypted: ")
text = text.lower()
shift = 5

alphabet = string.ascii_lowercase
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

encrypted = text.translate(table)

print(encrypted)
