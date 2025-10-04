#!/usr/bin/env python3
"""
secure_password_gen.py

Secure random password generator:
- User specifies length
- User can include uppercase, lowercase, digits, special characters
- Ensures each generated password is unique during the program session
- Uses only standard library (secrets, string)
- Optionally enforces at least one character from each selected category
"""

import secrets
import string
import sys

# Set of previously generated passwords (session-unique)
_generated_passwords = set()

# Default special characters
DEFAULT_SPECIALS = "!@#$%^&*()-_=+[]{}|;:,.<>?/`~"

def build_charset(use_upper: bool, use_lower: bool, use_digits: bool, use_special: bool, special_chars: str = DEFAULT_SPECIALS):
    parts = []
    if use_upper:
        parts.append(string.ascii_uppercase)
    if use_lower:
        parts.append(string.ascii_lowercase)
    if use_digits:
        parts.append(string.digits)
    if use_special:
        parts.append(special_chars)
    charset = "".join(parts)
    return charset, parts  # return parts so we can enforce one-of-each if needed

def possible_combinations_count(charset_len: int, length: int):
    # returns number of possible different passwords (int) = charset_len ** length
    return charset_len ** length

def generate_password(length: int,
                      use_upper: bool = True,
                      use_lower: bool = True,
                      use_digits: bool = True,
                      use_special: bool = True,
                      enforce_each_category: bool = True,
                      special_chars: str = DEFAULT_SPECIALS,
                      max_attempts: int = 10000) -> str:
    """
    Generate a secure random password with given options.
    Ensures uniqueness within this program session by checking _generated_passwords.
    If enforce_each_category is True, the password will include at least one char
    from each selected category (if possible given length).
    """
    if length <= 0:
        raise ValueError("Password length must be positive.")

    charset, parts = build_charset(use_upper, use_lower, use_digits, use_special, special_chars)
    if not charset:
        raise ValueError("At least one character class must be selected.")

    # Quick exhaustion check: if total possible combinations <= number of generated passwords, we cannot create a new unique one.
    total_possible = possible_combinations_count(len(charset), length)
    if total_possible <= len(_generated_passwords):
        raise RuntimeError("No more unique passwords possible with the chosen length and charset (session exhausted).")

    # If enforcing one-of-each-type, ensure length is sufficient
    required_types = len(parts)
    if enforce_each_category and length < required_types:
        raise ValueError(f"Length {length} is too short to include at least one character from each of the {required_types} selected categories.")

    attempts = 0
    while True:
        attempts += 1
        if attempts > max_attempts:
            raise RuntimeError("Failed to generate a unique password after many attempts. Try increasing length or altering charset.")
        # If enforcing each category, pick one from each selected part first, then fill rest from full charset
        if enforce_each_category and parts:
            pwd_chars = []
            for part in parts:
                # pick one guaranteed from each selected category
                pwd_chars.append(secrets.choice(part))
            remaining = length - len(pwd_chars)
            for _ in range(remaining):
                pwd_chars.append(secrets.choice(charset))
            # shuffle securely
            # simple Fisher-Yates using secrets.randbelow
            for i in range(len(pwd_chars)-1, 0, -1):
                j = secrets.randbelow(i+1)
                pwd_chars[i], pwd_chars[j] = pwd_chars[j], pwd_chars[i]
            candidate = "".join(pwd_chars)
        else:
            candidate = "".join(secrets.choice(charset) for _ in range(length))

        if candidate not in _generated_passwords:
            _generated_passwords.add(candidate)
            return candidate
        # else loop and try again

def interactive_cli():
    print("Secure Password Generator (session-unique, uses 'secrets')\n")

    try:
        length = int(input("Password length (e.g. 12): ").strip())
    except ValueError:
        print("Invalid length. Must be an integer.")
        return

    def ask_yesno(prompt: str, default: bool = True) -> bool:
        default_str = "Y/n" if default else "y/N"
        r = input(f"{prompt} [{default_str}]: ").strip().lower()
        if r == "":
            return default
        return r[0] == "y"

    use_upper = ask_yesno("Include UPPERCASE letters?", True)
    use_lower = ask_yesno("Include lowercase letters?", True)
    use_digits = ask_yesno("Include numbers?", True)
    use_special = ask_yesno("Include special characters (e.g. !@#$%)?", True)
    enforce_each = ask_yesno("Ensure at least one character from each selected type (recommended)?", True)

    # Optionally allow custom special chars
    custom_special = None
    if use_special:
        custom = input("Press ENTER to use default special characters or type custom specials: ").strip()
        if custom:
            custom_special = custom

    # How many passwords
    try:
        count = int(input("How many passwords to generate? (1): ").strip() or "1")
        if count <= 0:
            raise ValueError
    except ValueError:
        print("Invalid number of passwords.")
        return

    print("\nGenerated passwords:")
    for i in range(count):
        try:
            pwd = generate_password(length, use_upper, use_lower, use_digits, use_special, enforce_each, custom_special or DEFAULT_SPECIALS)
        except Exception as e:
            print(f"ERROR: {e}")
            break
        print(f"{i+1}. {pwd}")

    print("\nNote: passwords are guaranteed unique only within this program run (session).")

if __name__ == "__main__":
    # If script is run directly, start interactive CLI
    try:
        interactive_cli()
    except KeyboardInterrupt:
        print("\nAborted.")
        sys.exit(1)
