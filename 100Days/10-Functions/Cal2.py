def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: No se puede dividir por cero."

def calcular(operador, num1, num2):
    if operador == '+':
        return suma(num1, num2)
    elif operador == '-':
        return resta(num1, num2)
    elif operador == '*':
        return multiplicacion(num1, num2)
    elif operador == '/':
        return division(num1, num2)
    else:
        return "Operador no válido"

resultado = 0

while True:
    try:
        num = float(input("Ingrese un número: "))
        operador = input("Ingrese un operador (+, -, *, /) o '=' para obtener el resultado: ")
    except ValueError:
        print("Error: Ingrese un número válido.")
        continue
    
    if operador == '=':
        print(f"Resultado final: {resultado}")
        break
    
    if operador in ('+', '-', '*', '/'):
        resultado = calcular(operador, resultado, num)
        print(f"Resultado parcial: {resultado}")
    else:
        print("Operador no válido. Intente de nuevo.")
