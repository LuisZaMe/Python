import math

#Function that allow for input
def greet_with(name, location):
    print('hello,', name)
    print(f"What is it like in location : {location}")

# name = input('Dame tu nombre: ')
# location = input('Cual es tu ubicacion: ')
# greet_with(name="Luis", location="Mexico")

def paint_calc(test_h, test_w, cover):
    num_cans = test_h * test_w / cover
    round_up_cans = math.ceil(num_cans)
    return round_up_cans

# test_h = int(input('Height :'))
# test_w = int(input('Weight :'))
# coverage = 5

# print("El resultado es : ",paint_calc(test_h=2, test_w=4, cover=coverage))
# print("El resultado es : ",paint_calc(test_h, test_w, cover=coverage))

# Numeros primos
def prime_checker(number):
    is_prime = True
    
    for i in range(2,number):
        if number % i == 0:
            is_prime = False
    
    if is_prime:
        print('Es numero primo')
    else:
        print('No es numero primo')

    return is_prime
    
n = int(input('Pass Number :'))
prime_checker(number = n)

