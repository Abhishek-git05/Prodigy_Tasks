def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        # Encrypt lowercase letters
        elif char.islower():
            encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char  # Leave any non-letter characters unchanged
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    decrypted_text = ""
    for char in encrypted_text:
        # Decrypt uppercase letters
        if char.isupper():
            decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        # Decrypt lowercase letters
        elif char.islower():
            decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_text += char  # Leave any non-letter characters unchanged
    return decrypted_text

def main():
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value (a positive integer): "))
    
    encrypted = caesar_cipher_encrypt(text, shift)
    decrypted = caesar_cipher_decrypt(encrypted, shift)
    
    print("\nOriginal text:", text)
    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()
