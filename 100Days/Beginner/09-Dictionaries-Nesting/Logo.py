logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
def resta(a, b):
    return a - b

# Solicitar al usuario ingresar dos números
try:
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
except ValueError:
    print("Error: Ingrese números válidos.")
else:
    # Realizar la resta y mostrar el resultado
    resultado = resta(num1, num2)
    print(f"Resultado de la resta: {resultado}")
