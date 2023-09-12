# *******************************************************************************
# Empresa: OvniOn
#
# Aplicación: Juego Piedra, Papel o Tijera
#
# Destinado a: personas de todas las edades y niveles.
#
# Descripción del funcionamiento:
#   Permite ingresar una de las opciones. Luego se compara con la opción
#   seleccionada por la máquina. Entonces decide el ganador de la jugada
#   y le suma puntos. Al final de la partida informa quien es el ganador
#   y cuantos puntos obtuvieron los jugadores.
# *******************************************************************************

# Importar la clase random

import random

# Mostrar menú de opciones

while True:
    print("*************************************************")
    print("Bienvenido al juego Piedra, Papel o Tijera       ")
    print("                                                 ")
    print("                                creado por OvniOn")
    print("*************************************************")

    print("*************** MENÚ DE OPCIONES ****************")

    print("0- SALIR")
    print("1- INICIAR EL JUEGO")

    print("*************************************************")

    # Solicitar al usuario que ingrese un opción del menú y la guarda en la variable seleccion.

    seleccion = int(input("Ingrese una opción: "))

    if seleccion == 0:
        print("**********************************************")
        print("¡ Gracias por utilizar nuestro juego !")
        print("                                              ")
        print("Conozca más sobre nosotros en nuestra web:    ")
        print("                 ovnion.com")
        break

    elif seleccion == 1:
        user_puntos = 0
        computadora_puntos = 0
        opciones = ["piedra", "papel", "tijeras"]

        while True:
            user_input = input(
                "Tipea Piedra/Papel/Tijeras or S para salir: ").lower()

            if user_input == "s":
                break

            if user_input not in opciones:
                continue

            # Lógica para que la máquina elija una opción.
            # piedra: 0, papel: 1, tijeras: 2

            numero_random = random.randint(0, 2)

            computadora_elige = opciones[numero_random]

            print("Computadora elige", computadora_elige + ".")

            # Lógica dónde el usuario gana contra la máquina.

            if user_input == "piedra" and computadora_elige == "tijeras":
                print("Ganaste!")
                user_puntos += 1

            elif user_input == "papel" and computadora_elige == "piedra":
                print("Ganaste!")
                user_puntos += 1

            elif user_input == "tijeras" and computadora_elige == "papel":
                print("Ganaste!")
                user_puntos += 1

            # Lógica dónde el usuario empata contra la máquina.
            elif user_input == "piedra" and computadora_elige == "piedra":
                print("Empate!")

            elif user_input == "papel" and computadora_elige == "papel":
                print("Empate!")

            elif user_input == "tijeras" and computadora_elige == "tijeras":
                print("Empate!")

            else:  # Lógica dónde la máquina gana contra el usuario.
                print("Perdiste!")
                computadora_puntos += 1

        # Mostrar resultado final de la partida.

        print("****************************************************")
        print(
            f"Vos ganaste {user_puntos} veces || La computadora ganó {computadora_puntos} veces.")
        print("¡ Bien hecho, vuelve a intentarlo !")
