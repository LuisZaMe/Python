import string

direction = int(input("Type 'encode' to encrypt, type 'decode' to decrypt* :"))
userMessage = input('Type your message :').lower()
shiftNumber = int(input('Type the shift number:'))
alphabet = list(string.ascii_lowercase)

def encrypt(plain_text, shift_amount):
   encrypt_text = ''

   for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position + shift_amount

      if new_position > 26:
         new_position = new_position - 26

      new_letter = alphabet[new_position]
      encrypt_text += new_letter
           
   print(f"The encoded text is {encrypt_text}")

def decrypt(plain_text, shift_amount):
   position = 0
   decrypt_text = ''

   for letter in plain_text:
      position = alphabet.index(letter)
      new_position = position - shift_amount
      
      if new_position < 0:
         new_position = new_position + 26
      
      new_letter = alphabet[new_position]
      decrypt_text += new_letter
           
   print(f"The decoded text is {decrypt_text}")

if direction == 1: # Encriptar
   encrypt(userMessage, shiftNumber)

elif direction == 2: # Desencriptar
   decrypt(userMessage, shiftNumber)
else:
    print('Error')