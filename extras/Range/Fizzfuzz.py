inputnumber = int(input("Ingresa un nuermo para jugar fizzfuz: "))

for number in range(1,inputnumber+1):

    if number % 3 == 0 and number % 5 == 0:
        print("FizzFuzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 == 0:
        print("Fuzz")
    else :
        print(number)
    