import random
import string

def get_password_length():
    while True:
        try:
            length = int(input("Enter the password length: "))
            if length > 0:
                return length
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_character_set():
    print("Select character sets to include in the password:")
    print("1. Letters")
    print("2. Numbers")
    print("3. Symbols")
    print("4. All of the above")
    print("Enter your choices separated by commas (e.g., 1,2,3):")
    
    while True:
        choices = input("Enter your choice(s): ").split(',')
        choices = [choice.strip() for choice in choices]  # Remove any spaces
        valid_choices = {'1', '2', '3', '4'}
        if set(choices).issubset(valid_choices):
            return choices
        else:
            print("Invalid choices. Please enter 1, 2, 3, or 4, separated by commas.")

def generate_password(length, char_set):
    return ''.join(random.choice(char_set) for _ in range(length))

def main():
    length = get_password_length()
    choices = get_character_set()
    
    char_set = ""
    if '1' in choices:
        char_set += string.ascii_letters
    if '2' in choices:
        char_set += string.digits
    if '3' in choices:
        char_set += string.punctuation
    if '4' in choices:
        char_set = string.ascii_letters + string.digits + string.punctuation
    
    if not char_set:
        print("No character set selected. Using default (letters).")
        char_set = string.ascii_letters
    
    password = generate_password(length, char_set)
    print(f"Generated password: {password}")

if __name__ == "__main__":
    main()
