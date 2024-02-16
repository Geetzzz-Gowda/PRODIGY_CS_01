
def caesar_cipher(text, shift, encrypt=True):
    result = ''
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start) if encrypt else chr((ord(char) - start - shift) % 26 + start)
            result += shifted_char
        else:
            result += char
    return result
        
def main():
    while True:
        print("\nCaesar Cipher Menu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit") 
        
        choice = input("Select an option (1, 2, or 3): ")
        
        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher(message, shift)
            print("Encrypted message: ", encrypted_message)
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher(message, shift, encrypt=False)
            print("Decrypted message: ", decrypted_message)           
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
