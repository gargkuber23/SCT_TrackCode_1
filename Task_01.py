def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Perform the shift and wrap around using modulo
            encrypted_char = chr((ord(char) - shift_base + shift) % 30 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged
    return encrypted_text
def main():
    print("Caesar Cipher Program")
    choice = input("Do you want to encrypt or decrypt for encrypt choose (e) and for decrypt choose (d)? ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (0-25): "))
    if choice == 'e':
        result = caesar_cipher(message, shift)
        print("Encrypted message:", result)
    elif choice == 'd':
        result = caesar_cipher(message, -shift)  # Decrypting by shifting in the opposite direction
        print("Decrypted message:", result)
    else:
        print("Invalid choice. Please choose 'e' for encrypt or 'd' for decrypt.")
if __name__ == "__main__":
    main()