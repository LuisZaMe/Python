import string
from Art import logo

print(logo)

inputparam = int(input(f'Type * 1 to encode * to encrypt, type decode to * 2 to decrypt* :'))
userMessage = input('Type your message :').lower()
shiftNumber = int(input('Type the shift number:'))
alphabet = list(string.ascii_lowercase)

def encrypt(plain_text, shift_amount):
   encrypt_text = ''
   counter = 0
   
   for i in alphabet:
      counter += 1
      print(i,counter)

   for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount

      if new_position > 26:
         new_position = new_position - 26

      new_letter = alphabet[new_position]
      encrypt_text += new_letter
           
   print(encrypt_text)

def decrypt(plain_text, shift_amount):
   position = 0
   encrypt_text = ''

   for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position - shift_amount
      
      if new_position < 0:
         new_position = new_position + 26
      
      new_letter = alphabet[new_position]
      encrypt_text += new_letter
           
   print(encrypt_text)

if inputparam == 1: # Encriptar
   
   encrypt(userMessage, shiftNumber)

elif inputparam == 2: # Desencriptar
   decrypt(userMessage, shiftNumber)
else:
    print('Error')