import os
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []

def sum_values(sum_values):
    sum = 0
    for i in sum_values:
        sum = sum + i
 
    return(sum)

def begin_game():
    os.system('cls')
    text = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ").lower()
    if text == 'y':
        main_blackjack()
    else:
        print('Thats too bad, maybe next time =(...') 

def computer_plays(user_count):

    computer_count = sum_values(computer_cards)

    if user_count <= 21:
        
        while computer_count < 18:
           computer_cards.append(random.choice(cards))  ## 8, 5, 5
           computer_count = sum_values(computer_cards)
           
        if user_count > computer_count or computer_count > 21:
            print('You win !!')
        elif user_count == computer_count:
            print('Draw')
        else:
            print('Computer B wins !!')

    else:
        print('Computer A wins')

    print('Computers cards: ', computer_cards, 'Current Score :', computer_count)


def main_blackjack():
    user_count = 0

    for usr in range(2):
        user_cards.append(random.choice(cards))

    for com in range(1):
        computer_cards.append(random.choice(cards))
    
    user_count = sum_values(user_cards)

    print('*************************************************************************************')
    print('Computers first card: ', computer_cards, 'Current Score :', sum_values(computer_cards))
    print('                                                                                     ')

    while True: 
      print('Your cards: ', user_cards, 'Current Score :', user_count)
      extraCard =  input("Type 'y' to get another card, type 'n' : ").lower()
   
      if extraCard == 'y': ## 9, 8
         user_cards.append(random.choice(cards))  ## 8, 5, 5
         user_count = sum_values(user_cards)
         if user_count > 21:  ## 18
            print('Your cards: ', user_cards, 'Current Score :', user_count)
            break          
         else:            
            continue
      else:
         break

    computer_plays(user_count)


begin_game()


