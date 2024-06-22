import string
from art import logo
print(logo)

alphabet = list(string.ascii_lowercase)
numbers = list(str(range(10)))
symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt* :")
text = input('Type your message :').lower()
shift = int(input('Type the shift number:'))

def caesar(start_text, shift_amount, cipher_direction):
   end_text = ""
 
   if cipher_direction == 'decode':
      shift_amount *= -1

   for char in start_text:
      
      if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        
        if new_position < 0:
            new_position = new_position + 26
        elif new_position > 26:
            new_position = new_position - 26
      else:
         end_text += char
      
      end_text += alphabet[new_position]
           
   print(f"The {direction}d text is {end_text}")

shift = shift % 26
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)