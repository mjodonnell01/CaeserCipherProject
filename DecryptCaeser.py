#Decrypt Caeser Cipher
#Michael O'Donnell
#Follow along: https://www.scaler.com/topics/caesar-cipher-python/

def decrypt():
    # Enter encrypted message that was received
    encrypted_message = input("Enter message: ")

    # Enter shift pattern key
    k = int(input("Enter key: "))
    decrypted_message = ""

    for ch in encrypted_message:
        # Check if character is lowercase
        if ch.islower():
            position = ord(ch) - ord('a')
            new_pos = (position - k) % 26
            new_char = chr(new_pos + ord('a'))
            decrypted_message += new_char
        # Check if character is uppercase
        elif ch.isupper():
            position = ord(ch) - ord('A')
            new_pos = (position - k) % 26
            new_char = chr(new_pos + ord('A'))
            decrypted_message += new_char
        # Handle spaces and non-alphabetic characters
        else:
            decrypted_message += ch

    print("Decrypted message is: " + decrypted_message)
    
decrypt()
