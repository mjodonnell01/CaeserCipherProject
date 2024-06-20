#Caeser encrpytion
#Michael O'Donnell
#Followed Along: https://www.scaler.com/topics/caesar-cipher-python/

def encrypt_text(plaintext, n):
    ans = ""

    # Loop through entered text
    for i in range(len(plaintext)):
        ch = plaintext[i]

        # Check if space is there, add space if so
        if ch == " ":
            ans += " "

        # Check if character is uppercase, then encrypt
        elif ch.isupper():
            ans += chr((ord(ch) + n - 65) % 26 + 65)

        # Check if character is lowercase
        elif ch.islower():
            ans += chr((ord(ch) + n - 97) % 26 + 97)

        # If the character is neither (e.g., punctuation), just add it as is
        else:
            ans += ch

    return ans

# Getting user input
plaintext = input("Enter your message to encrypt: ")
n = int(input("Please input encryption key as an integer: "))

print("Plain Text is : " + plaintext)
print("Shift pattern is : " + str(n))
print("Cipher Text is : " + encrypt_text(plaintext, n))
