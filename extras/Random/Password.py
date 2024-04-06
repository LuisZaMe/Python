import string
import random

# x = [1 ,2 ,3 ,4 ,5]
# random.shuffle(x)
# print(x)

# Create a list with all lowercase letters from 'a' to 'z'
letters = list(string.ascii_lowercase)
numbers = list(str(range(10)))
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to the PyPassword Generator!")
nr_letters=int(input("How many letters would you like in your password?\n"))
nr_numbers=int(input(f"How many numbers would you like ?\n"))
nr_symbols=int(input(f"How many symbols would you like ?\n"))
random_char = ''
password_list = []

# Easy level
# for letter in range(0, nr_letters):
#     random_char += random.choice(letters)

# for number in range(0, nr_numbers):
#     random_char += random.choice(str(numbers))

# for symbol in range(0, nr_symbols):
#     random_char += random.choice(symbols)
# print(random_char)

# Hard level
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for number in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
for char in password_list:
    random_char += char   

print(random_char)