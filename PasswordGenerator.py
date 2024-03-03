import string
import random

def generate_password(length, use_uppercase=True, use_numbers=True, use_punctuation=True):

    characters = string.ascii_letters
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_punctuation:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))

if __name__ == "__main__":
    length = int(input("Enter the length of the password: "))
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == "y"
    use_numbers = input("Include numbers? (y/n): ").lower() == "y"
    use_punctuation = input("Include punctuation? (y/n): ").lower() == "y"
    print(f"your generated password is {generate_password(length, use_uppercase, use_numbers, use_punctuation)}")