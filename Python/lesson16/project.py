import random
import string

def generate_strong_password(length=12):
    """
    Generates a random password composed of lowercase, uppercase, digits, and punctuation.

    Args:
        length (int): The desired length of the password. Defaults to 12.

    Returns:
        str: A randomly generated strong password.
    """
    if length < 8:
        print("Warning: A password length of less than 8 characters is not recommended for security.")

    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage:
new_password = generate_strong_password()
print(f"Your new strong password is: {new_password}")

# You can also specify a different length:
another_password = generate_strong_password(length=16)
print(f"Another strong password (16 characters): {another_password}")