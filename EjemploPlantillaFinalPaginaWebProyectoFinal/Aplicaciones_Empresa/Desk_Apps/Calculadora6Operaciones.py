import math

# Calculadora para realizar operaciones matemáticas (6)

while True:
    print("**********************************************")
    print("Bienvenido a la calculadora de 6 operaciones")
    print(""                                              )
    print("                             creado por OvniOn")
    print("**********************************************")

    print("************ MENÚ DE OPERACIONES **************")

    print("1- SUMAR 2 NÚMEROS")
    print("2- RESTAR 2 NÚMEROS")
    print("3- MULTIPLICAR 2 NÚMEROS")
    print("4- DIVIDIR 2 NÚMEROS")
    print("5- ELEVAR UN NÚMERO")
    print("6- APLICAR LA RAÍZ CUADRADA A UN NÚMERO")
    print("0- SALIR")

    print("**********************************************")

    opcion = int(input("Ingrese una opción de operación: "))

    # Comienza la lógica del programa.

    if opcion == 0:
        print("**********************************************")
        print("¡ Gracias por utilizar nuestra calculadora !"  )
        print("                                              ")
        print("Conozca más sobre nosotros en nuestra web:    ")
        print("                 ovnion.com"                   )
        break

    elif opcion >= 1 and opcion <= 6:

        print("************* Inicia aplicación *************")

        if opcion == 1:
            numero1 = int(input("Ingrese el primer número --> "))
            numero2 = int(input("Ingrese el segundo número --> "))

            suma = numero1 + numero2

            print("**********************************************")
            print(f"El resultado de sumar {numero1} y {numero2} es: {suma}")

        elif opcion == 2:
            numero1 = int(input("Ingrese el primer número --> "))
            numero2 = int(input("Ingrese el segundo número --> "))

            resta = numero1 - numero2

            print("**********************************************")
            print(f"El resultado de restar {numero1} y {numero2} es: {resta}")

        elif opcion == 3:
            numero1 = int(input("Ingrese el primer número --> "))
            numero2 = int(input("Ingrese el segundo número --> "))

            multiplicacion = numero1 * numero2

            print("**********************************************")
            print(
                f"El resultado de multiplicar {numero1} y {numero2} es: {multiplicacion}")

        elif opcion == 4:
            numero1 = int(input("Ingrese el primer número --> "))
            numero2 = int(input("Ingrese el segundo número --> "))

            division = numero1 / numero2

            print("**********************************************")
            print(
                f"El resultado de dividir {numero1} y {numero2} es: {division}")

        elif opcion == 5:
            numero1 = int(input("Ingrese el número base de la potencia --> "))
            numero2 = int(
                input("Ingrese el número exponente de la potencia --> "))

            potenciacion = math.pow(numero1, numero2)

            print("**********************************************")
            print(
                f"El resultado de elevar {numero1} a {numero2} es: {potenciacion}")

        elif opcion == 6:
            numero1 = int(input("Ingrese el número base de la raíz --> "))

            radicacion = math.sqrt(numero1)

            print("**********************************************")
            print(
                f"El resultado de la raí cuadrada de {numero1} es: {radicacion}")
    else:
        print("¡ ATENCIÓN ! Ingresó una opción incorrecta. Vuelvalo a intentar.")
