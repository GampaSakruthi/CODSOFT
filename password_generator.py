import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Welcome to the Alphanumeric Password Generator!") 
    while True:
        try:
            length_str = input("\nEnter the desired length of the password (minimum 6 characters): ").strip()
            if length_str.isdigit():
                length = int(length_str)
            else:
                raise ValueError("Invalid input. Please enter a valid number.")
            if length < 6:
                print("Password length should be at least 6 characters.")
                continue
            password = generate_password(length)
            print(f"\nGenerated Password: {password}")
            choice = input("\nGenerate another password? (yes/no): ").lower()
            if choice != 'yes':
                break
        except ValueError as ve:
            print(ve)
if __name__ == "__main__":
    main()
