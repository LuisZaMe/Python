import random

numero=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

rock = (
    "    ______\n"
    "---'   ____)\n"
    "      (_____) \n"
    "      (_____) \n"
    "      (____) \n"
    "---._(____)"
)
paper = (
    "     ____\n"
    "----' ___)_____\n"
    "        _______)\n"
    "       _______)\n"
    "     _______)\n"
    "---.______)"
)

scissors = (
    "     ___\n"
    "---'   _)_____\n"
    "         ______)\n"
    "         _______)\n"
    "      (___)\n"
    "---._(___)"
)

if numero == 0:
    print (rock)

elif numero == 1:

    print (paper)  

elif numero == 2:

    print (scissors)

print("Computer chose:")

rps = random.randint (0,2)


if rps == 0:
    
    print (rock)

elif rps == 1:

    print (paper)
   
elif rps == 2:

 print (scissors)

if numero == 0 and rps == 0:
    print("Draw")
elif numero == 0 and rps == 1:
    print("Lost")
elif numero == 0 and rps == 2:
    print("Win")
elif numero == 1 and rps == 1:
    print("Draw")
elif numero == 1 and rps == 2:
    print("Lost")
elif numero == 1 and rps == 0:
    print("Win")
elif numero == 2 and rps == 2:
    print("Draw")
elif numero == 2 and rps == 0:
    print("Lost")
elif numero == 2 and rps == 1:
    print("Win")