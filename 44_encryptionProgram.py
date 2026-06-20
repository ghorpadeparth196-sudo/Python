#Encryption program
import random
import string

#printing all the characters and symbols etc..
char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()
random.shuffle(key)
# print(char)
# print(key)

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")          #Input from the user
cipher_text = ""                                            #Store encrypted result
for letter in plain_text:                                   #Convert each character into its encrypted equivalent
    index = char.index(letter)
    cipher_text += key[index]
print(f"Original message: {plain_text}")                    #Display orignal message
print(f"Encrypted message: {cipher_text}")                  #Display encrypted message

#DECRYPT
cipher_text = input("Enter a message to encrypt: ")         #Input from the user
plain_text = ""                                             #Store decrypted result:-
for letter in cipher_text:
    index = key.index(letter)
    plain_text += char[index]
print(f"Encrypted message: {cipher_text}")                  #Display decrypted message
print(f"Original message: {plain_text}")                    #Display orignal message