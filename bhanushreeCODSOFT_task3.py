import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not any([use_uppercase, use_lowercase, use_digits, use_symbols]):
        raise ValueError("At least one character type (uppercase, lowercase, digits, symbols) must be selected.")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Welcome to Advanced Password Generator!")
    
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Length should be a positive integer. Please try again.")
                continue
            
            use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
            use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
            use_digits = input("Include digits? (yes/no): ").lower() == 'yes'
            use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'
            
            password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_symbols)
            print(f"Generated Password: {password}")
            
            choice = input("Do you want to generate another password? (yes/no): ").lower()
            if choice != 'yes':
                print("Thank you for using Advanced Password Generator!")
                break
        
        except ValueError as ve:
            print(f"Error: {str(ve)} Please select at least one character type.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
