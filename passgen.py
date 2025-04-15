import random
import string

def generate_password(length, use_upper=True, use_digits=True, use_symbols=True):
    characters = string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

while True:
    user_input = input("Enter the length of your password: ")

    try:
        choices = int(user_input)
        print("Your password:", generate_password(choices))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        
    should_continue = input('Do you want to create a new password?(y/n: )').lower()
    if should_continue == 'n':
        print('Goodbye')
        break