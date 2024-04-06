import os
from Logo import logo

print(logo)
print('Welcome to the secret auction program')

bidders_dictionary = {}
is_condition_met = False

while not is_condition_met:
    input_name = input('What is your name? : ')
    input_bid = int(input('What is bid? :'))
    bidders_dictionary[input_name] = input_bid
    input_add_bidder = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if input_add_bidder == 'no':
        is_condition_met = True
        os.system('cls')

        # Find the highest bidder and their bid
        highest_bidder = max(bidders_dictionary, key=bidders_dictionary.get)
        highest_bid = bidders_dictionary[highest_bidder]

        # Print the result
        print(f'The highest bidder is {highest_bidder} with a bid of ${highest_bid}.')
    else:
        os.system('cls')
