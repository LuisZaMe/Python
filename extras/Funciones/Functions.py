import math
# def greet  (name):
#     print("Hello :",name)
#     print(f"Hello : {name}")
    
# # name = input("whats your name?")
# # greet(name)

# def greet_with(name,location):
#     print("Hello :",name)
#     print(f"what is it like it location : {location}")

# # name = input("whats your name?")
# # location = input("whats your location?")
# # greet(name,location)


# def pain_cal(test_h,test_w,cover):
#     num_cans = test_h * test_w / cover
#     round_up_cans = math.ceil(num_cans)
#     return round_up_cans

# test_h = int(input())
# test_w = int(input())
# coverage = 5

# print("El resultado es : ",pain_cal(test_h,test_w,cover=coverage))

#Numeros primos
def prime_checker(number):
    is_prime = True

    for i in range (2,number):
        if number %i == 0:
            is_prime =False

    if is_prime:
            print("Es numero primo")
    else:
         print("no es numero primo")
         

    return is_prime

n = int(input("pas number : "))
prime_checker(number=n)