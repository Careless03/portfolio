import random
import string

how_much_padding = 10
padding =''

for _ in range(how_much_padding):
    padding += random.choice(string.ascii_letters + string.digits + string.punctuation)

print(padding)