import random

word_list = ["gato", "oro", "sol", "juego", "flor", "piel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

print('Pssst, the solution is: ', chosen_word)
guess = input("Guess a letter:").lower()

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
       display[position] = letter

print(display)

#Replacing blanks
        