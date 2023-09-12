# *******************************************************************************
# Empresa: OvniOn
#
# Aplicación: Elige tu propia aventura
#
# Destinado a: personas de todas las edades y niveles.
#
# Descripción del funcionamiento:
#   Luego de leer un texto de aventura permite ingresar opciones para
#   continuar avanzando con la historia. En función de las opciones
#   decididas por el usuario, la máquina muestra continuar o finalizar
#   la aventura.
# *******************************************************************************

while True:

    print("*************************************************")
    print("Bienvenido al juego Elige tu propia aventura     ")
    print("                                                 ")
    print("                                creado por OvniOn")
    print("*************************************************")

    print("************ MENÚ DE OPERACIONES **************")

    print("0- SALIR")
    print("1- INICIAR LA APLICACIÓN")

    print("**********************************************")

    opcion = int(input("Ingrese una opción de operación: "))

    if opcion == 0:
        print("**********************************************")
        print("¡ Gracias por utilizar nuestro juego !")
        print("                                              ")
        print("Conozca más sobre nosotros en nuestra web:    ")
        print("                 ovnion.com"                   )
        break

    elif opcion == 1:
        nombre = input("Ingresa tu nombre: ")
        print("Bienvenido", nombre, "a esta aventura!")

        respuesta = input(
            "Estás en un camino de tierra, ha llegado a su fin y puedes ir a izquierda o derecha. ¿Qué camino te gustaría tomar? ").lower()

        if respuesta == "izquierda":
            respuesta = input(
                "Cuando llegas a un río, ¿puedes rodearlo o cruzarlo nadando? Escriba caminar para caminar y nadar para cruzar a nado: ")

            if respuesta == "nadar":
                print("Cruzaste nadando y fuiste devorado por un caimán.")
            elif respuesta == "caminar":
                print(
                    "Caminaste muchos kilómetros, te quedaste sin agua y perdiste el juego.")
            else:
                print('No es una opción válida. Quedás afuera del juego.')

        elif respuesta == "derecha":
            respuesta = input(
                "Llegas a un puente, parece tambaleante, ¿quieres cruzarlo o regresar (cruzar/atrás)?")

            if respuesta == "atrás":
                print("Volviste y perdiste el juego.")
            elif respuesta == "cruzar":
                respuesta = input(
                    "Cruzas el puente y te encuentras con un extraño. ¿Hablas con ellos (si/no)?")

                if respuesta == "si":
                    print("Hablas con el extraño y te dan oro. ¡Tú ganas!")
                elif respuesta == "no":
                    print("Ignoras al extraño, se ofende y pierdes.")
                else:
                    print('No es una opción válida. Quedás afuera del juego.')
            else:
                print('No es una opción válida. Quedás afuera del juego.')

        else:
            print('No es una opción válida. Quedás afuera del juego.')

        print("Gracias por jugar con nuestro juego", nombre)
