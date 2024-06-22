import os
from art import logo

print(logo)
print("Bienvenido a Calculadora")

def Suma(a, b):
    return a + b

def Resta(a ,b):
    return b - a

def Multiplicaion(a ,b):
    return a * b

is_condition_met = False
resultado = 0
valor = ""

while not is_condition_met:
    a = int(input("dame numero: "))
    opc = input("+ - =: ")
    os.system('cls')

    if opc == '=':
        valor = valor + str(a) + opc
        print(valor)
        print(resultado)
        is_condition_met = True
        
    elif opc == '+':
        valor = valor + str(a) + opc
        print(valor)
        resultado = Suma(a, resultado)
        
    elif opc == '-':

        valor = valor + str(a) + opc
        print(valor)
        resultado = Resta(resultado, a)
        print(f"Resultado de la resta: {resultado}")
    elif opc == '*':
        valor = valor + str(a) + opc
        print(valor)
        resultado = Multiplicaion(a, resultado)
        
    else:
         print("Operador no válido. Intente de nuevo.")
