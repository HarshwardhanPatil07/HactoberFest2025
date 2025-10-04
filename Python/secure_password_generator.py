"""
GitHub Username: Shivi2705
Aim: Generate secure random passwords with user-defined options
Date: October 4, 2025
"""

import random
import string

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_special=True):
    """Generate a secure random password based on user choices."""
    
    if length <= 0:
        raise ValueError("Password length must be greater than 0")
    
    # Character pools
    upper = string.ascii_uppercase if use_upper else ''
    lower = string.ascii_lowercase if use_lower else ''
    digits = string.digits if use_digits else ''
    special = "!@#$%^&*()-_=+[]{}|;:,.<>?/" if use_special else ''
    
    all_chars = upper + lower + digits + special
    if not all_chars:
        raise ValueError("At least one character type must be selected")
    
    # Ensure at least one character from each selected type
    password = []
    if use_upper:
        password.append(random.choice(upper))
    if use_lower:
        password.append(random.choice(lower))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special))
    
    # Fill the remaining length
    while len(password) < length:
        password.append(random.choice(all_chars))
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    return ''.join(password)

def main():
    print("=== Secure Random Password Generator ===")
    
    length = int(input("Enter password length: "))
    
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    print(f"\n🔐 Generated Password: {password}")

if __name__ == "__main__":
    main()
