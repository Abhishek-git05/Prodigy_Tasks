import string

def assess_password_strength(password):
   
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, score

def main():
    print("Password Strength Assessment Tool")
    print("Criteria:")
    print("- Minimum length of 8 characters")
    print("- Includes uppercase and lowercase letters")
    print("- Includes at least one digit")
    print("- Includes at least one special character")
    print()

    password = input("Enter your password to assess its strength: ")
  
    strength, score = assess_password_strength(password)
 
    print(f"Password Strength: {strength}")
    print(f"Score: {score}/6")

if __name__ == "__main__":
    main()
