import os

def limpiar_pantalla():
    # Comprobamos el sistema operativo para determinar el comando de limpieza adecuado
    sistema_operativo = os.name

    if sistema_operativo == 'posix':  # Linux y macOS
        os.system('clear')
    elif sistema_operativo == 'nt':  # Windows
        os.system('cls')
    else:
        # Si el sistema operativo no es ni Linux/macOS ni Windows, no se realiza ninguna acción
        pass

# Llama a la función para limpiar la pantalla
limpiar_pantalla()
