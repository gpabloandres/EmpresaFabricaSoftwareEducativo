#*******************************************************************************
# Empresa: OvniOn
# 
# Aplicación: Calculadora de promedios de notas
# 
# Destinado a: estudiantes de todas las edades y niveles.
# 
# Descripción del funcionamiento:
#   Permite ingresar la cantidad de asignaturas y sus nombres. Luego
#   solicita al usuario que ingrese la nota de cada asignatura. Entonces permite
#   calcula el promedio de las notas ingresadas y muestra en pantalla
#   el promedio calculado con un mensaje informativo.
#*******************************************************************************

while True:

    print("*************************************************")
    print("Bienvenido a la calculadora de promedios de notas")
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
            print("¡ Gracias por utilizar nuestra calculadora !"  )
            print("                                              ")
            print("Conozca más sobre nosotros en nuestra web:    ")
            print("                 ovnion.com"                   )
            break

    elif opcion == 1:
    
        # Inicializar variables a utilizar

        lista_materias = []
        contador = 1
        cantidad_asignaturas = int(input("Ingrese la cantidad de materias que cargará: "))
        suma_notas = 0

        print("***************** Inicia aplicación **************")

        # Registrar en una lista las materias.

        while(contador <= cantidad_asignaturas):
            materia = input(f"Ingrese el nombre de la materia {contador}: ")
            lista_materias.append(materia)
            contador+=1

        print("***************** Carga de notas *****************")

        # Ingresar las notas de cada materia.

        for materia in lista_materias:
            nota = float(input(f"Ingrese la nota de la asignatura {materia}: "))
            suma_notas += nota

        # Calcular el promedio de todas las materias.

        promedio = suma_notas / cantidad_asignaturas

        print("************ Obtención del promedio de notas **************")

        # Mostrar el promedio obtenido.

        print(f"El promedio de notas las materias {lista_materias} es: {promedio}")
