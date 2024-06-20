#Brute Force Caeser Cipher
#Michael O'Donnell
#Followed along: https://www.scaler.com/topics/caesar-cipher-python/
message = input("Enter encrypted message: ")
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

for key in range(26):
    translated = ''
    for ch in message:
        if ch in uppercase_letters:
            num = uppercase_letters.find(ch)
            num = (num - key) % 26
            translated += uppercase_letters[num]
        elif ch in lowercase_letters:
            num = lowercase_letters.find(ch)
            num = (num - key) % 26
            translated += lowercase_letters[num]
        else:
            translated += ch
    print("Hacking key is " + str(key) + ": " + translated)
