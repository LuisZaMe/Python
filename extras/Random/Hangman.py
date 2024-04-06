import random

def seleccionar_palabra():
    palabras = ["python", "programacion", "hangman", "desarrollo", "aprender", "divertido", "codigo", "computadora"]
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def mostrar_monito(intentos):
    dibujo_monito = [
        '''
         -----
         |   |
             |
             |
             |
             |
        ''',
        '''
         -----
         |   |
         O   |
             |
             |
             |
        ''',
        '''
         -----
         |   |
         O   |
         |   |
             |
             |
        ''',
        '''
         -----
         |   |
        \O   |
         |   |
             |
             |
        ''',
        '''
         -----
         |   |
        \O/  |
         |   |
             |
             |
        ''',
        '''
         -----
         |   |
        \O/  |
         |   |
        /    |
             |
        ''',
        '''
         -----
         |   |
        \O/  |
         |   |
        / \\  |
             |
        '''
    ]
    return dibujo_monito[intentos]

def jugar_ahorcado():
    palabra_secreta = seleccionar_palabra()
    letras_adivinadas = []
    intentos_maximos = 6
    intentos = 0

    print("¡Bienvenido al juego de Hangman!")

    while True:
        print(mostrar_monito(intentos))
        print(mostrar_tablero(palabra_secreta, letras_adivinadas))

        letra = input("Ingresa una letra: ").lower()

        if letra in letras_adivinadas:
            print("Ya has adivinado esa letra. Intenta con otra.")
            continue

        letras_adivinadas.append(letra)

        if letra not in palabra_secreta:
            intentos += 1
            print(f"Incorrecto. Te quedan {intentos_maximos - intentos} intentos.")

        if set(letras_adivinadas) == set(palabra_secreta):
            print("¡Felicidades! Has adivinado la palabra.")
            break

        if intentos == intentos_maximos:
            print(mostrar_monito(6))
            print(f"¡Perdiste! La palabra era '{palabra_secreta}'.")
            break

if __name__ == "__main__":
    jugar_ahorcado()
