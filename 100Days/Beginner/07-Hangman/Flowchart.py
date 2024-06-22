import random

# Lista de palabras para el juego del ahorcado
palabras = ["gato", "oro", "sol", "juego", "flor", "piel"]

def elegir_palabra(palabras):
    return random.choice(palabras)

def mostrar_tablero(palabra, letras_correctas):
    tablero = ""
    for letra in palabra:
        if letra in letras_correctas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero

def jugar_ahorcado():
    palabra_secreta = elegir_palabra(palabras)
    letras_adivinadas = []
    intentos = 5  # Número de intentos permitidos

    print("¡Bienvenido al juego del ahorcado!")
    print("Adivina la palabra: ")
    print(mostrar_tablero(palabra_secreta, letras_adivinadas))

    while intentos > 0:
        adivinanza = input("Ingresa una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha(): # isalpha validates a-z o A-Z returns true
            print("Ingresa una sola letra válida.")
            continue

        if adivinanza in letras_adivinadas:
            print("Ya has adivinado esa letra.")
            continue

        letras_adivinadas.append(adivinanza)

        if adivinanza not in palabra_secreta:
            intentos -= 1
            print(f"¡Incorrecto! Te quedan {intentos} intentos.")
        
        print(mostrar_tablero(palabra_secreta, letras_adivinadas))

        # Verificar si se ha adivinado la palabra completa
        if all(letra in letras_adivinadas for letra in palabra_secreta):
            print("¡Felicidades! ¡Has adivinado la palabra!")
            break

    if intentos == 0:
        print(f"¡Perdiste! La palabra era '{palabra_secreta}'.")

# Iniciar el juego
jugar_ahorcado()
