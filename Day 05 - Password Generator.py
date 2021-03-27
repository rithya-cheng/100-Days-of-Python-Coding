import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F','G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbol = ['!', '@', '#', '%', '^', '&', '*', '+', '-']
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like in your password? "))
nr_numbers = int(input("How many numbers would you like in your password? "))
password_list = []
for char in range(0, nr_letters):
    password_list += random.choice(alphabet)
for char in range(0, nr_symbols):
    password_list += random.choice(symbol)
for char in range(0, nr_numbers):
    password_list += random.choice(number)
random.shuffle(password_list)
# print(password_list)
password = ""
for char in password_list:
    password += char
print(f"Your password is: {password}")