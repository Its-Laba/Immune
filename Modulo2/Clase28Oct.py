"""
    Ejercicios vistos en la clase del 28 de Octubre
"""


def ejer_1():
    """
    Ejercicio 1
    Escribir un programa que pida al usuario dos números y devuelva su división. Si el
    divisor es cero deberá mostrar un mensaje de error
    """
    dividendo = float(input("Introduzca número 1: "))
    divisor = float(input("Introduzca número 2: "))
    if divisor == 0:
        print("ERROR: Divisor no puede ser igual a 0")
    else:
        print(f"{dividendo}/{divisor} = {dividendo/divisor}")


def ejer_2():
    """
    Ejercicio 2
    Escribir un programa que pida al usuario un número entero y muestre por pantalla
    si es par o impar
    """
    n = int(input("Introduzca un número entero: "))
    if n % 2 == 0:
        print(f"El número {n} es par.")
    else:
        print(f"El número {n} es impar.")


def ejer_3():
    """
    Ejercicio 3
    Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla
    el tipo impositivo que le corresponde.
    """
    renta = float(input("Introduzca su renta: "))
    tipo_impositivo = 45
    if renta <= 60000:
        tipo_impositivo = 30
    if renta < 35000:
        tipo_impositivo = 20
    if renta < 20000:
        tipo_impositivo = 10
    if renta < 10000:
        tipo_impositivo = 5
    print(f"Su tipo impositivo es de {tipo_impositivo}%")


def ejer_4():
    """
    Ejercicio 4
    Escribir un programa para una empresa que tiene salas de juegos recreativos para
    todas las edades y quiere calcular de forma automática el precio que debe cobrar a
    sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y
    mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis,
    si tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€
    """

    edad = int(input("Introduzca edad del cliente:\t"))
    if edad < 4:
        print("Puede entrar gratis")
    else:
        precio = 5
        if 18 < edad:
            precio = 10
        print(f"El precio de la entrada es de {precio}$")


def ejer_5():
    """
    Ejercicio 5
    Escribir un programa que lea la puntuación del usuario e indique su nivel de
    rendimiento, así como la cantidad de dinero que recibirá el usuario.
    """
    score = float(input("Introduzca la puntuación del usuario:\t"))
    bonus = 2400
    if score < 0.4:
        bonus = bonus * 0
    elif score < 0.6:
        bonus = bonus * 0.4
    else:
        bonus = bonus * 0.6
    print(f"El usuario recibe la cantidad de {bonus} debido a su rendimiento")


def ejer_6():
    """
    Ejercicio 6
    Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no,
    y en función de su respuesta le muestre un menú con los ingredientes disponibles
    para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
    tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la pizza
    elegida es vegetariana o no y todos los ingredientes que lleva.
    """
    if input("¿Quiere una pizza vegetariana? (Y/N)\n").__eq__("Y"):
        topping = input("Elija ingrediente para su pizza:\n"
                        "Pimiento\n"
                        "Tofu\n")
        print(f"Pizza Vegetariana con {topping}")
    else:
        topping = input("Elija ingrediente para su pizza:\n"
                        "Peperoni\n"
                        "Jamón\n"
                        "Salmón\n")
        print(f"Pizza No Vegetariana con {topping}")


def ejer_7():
    """
    Ejercicio 7
    Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
    el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M
    y los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
    programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el
    grupo que le corresponde.
    """
    nombre = input("Introduzca nombre:\t")
    hombre = input("Introduzca sexo: (M/F)\t")
    if hombre.upper().__eq__("M"):
        hombre = True
    else:
        hombre = False

    letra = ord(nombre.strip()[0].upper())
    if (hombre and letra > 78) or (not hombre and letra < 77):
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")


def reto_if():
    """
    RETO IF
    Se debe comenzar por solicitar al usuario que ingrese la fecha actual en formato
    "día, DD/MM", donde [día] es un día de la semana, DD es el número de día y MM es
    el número de mes. Si el usuario ingresa un día de la semana inexistente o una
    fecha cuyo día supere el número 31 o el mes supere el número 12, finalizará el
    programa indicando que se produjo un error. Debe permitirse que ingrese el día
    de la semana en minúsculas o mayúsculas indistintamente. Como precondición se
    tiene que lo ingresado por el usuario tendrá la forma <[alfanumérico],
    [numérico]/[numérico]>.
    Una vez indicada la fecha, el usuario necesita poder indicar si ese día se tomaron
    exámenes, pero eso sólo si se trata de los niveles inicial, intermedio o avanzado, ya
    que las prácticas habladas y el inglés para viajeros no tienen exámenes. Si hubo
    exámenes, el usuario ingresará cuántos alumnos aprobaron y cuántos no, y el
    programa le mostrará el porcentaje de aprobados.
    Si el día fue el correspondiente a práctica hablada, el usuario deberá ingresar el
    porcentaje de asistencia a clase y el programa le indicará "asistió la mayoría" en
    caso de que la asistencia sea mayor al 50% o "no asistió la mayoría" si no es así.
    Si se trata del inglés para viajeros y la fecha actual corresponde al día 1 del mes 1 o
    del mes 7, se deberá imprimir "Comienzo de nuevo ciclo" y solicitar al usuario que
    ingrese la cantidad de alumnos del nuevo ciclo y el precio en € por cada alumno,
    para luego imprimir el ingreso total en €
    """
    fecha = input("Introduzca dia de la semana en formato (dia, DD/MM):\t ")
    dia_letra = fecha[:fecha.find(",")]
    dia_num = fecha[fecha.find(",")+1: fecha.find("/")].strip()
    mes = fecha[fecha.find("/")+1:]
    tipo = -1

    # Caso Error 1
    if not (dia_letra.isalnum() and dia_num.isnumeric() and mes.isnumeric()):
        print("El formato no es valido debe ser: <[alfanumérico], [numérico]/[numérico]>.")
        exit()
    # Caso Error 2
    if int(dia_num) < 0 or int(mes) < 0:
        print("la fecha no puede ser negativa.")
        exit()
    # Caso Error 3
    if int(dia_num) > 31:
        print("ERROR: El día no puede exceder de 31.")
        exit()
    # Caso Error 4
    if int(mes) > 12:
        print("ERROR: El mes no puede exceder de 12.")
        exit()
    # Caso Error 5
    if int(dia_num) > 29 and int(mes) == 2:
        print("ERROR: Febrero no puede tener mas de 29 dias.")
        exit()
    # Caso Error 6
    if int(dia_num) == 31 and ((int(mes) % 2 == 0 and int(mes) <= 7) or (int(mes) >= 8 and int(mes) % 2 == 1)):
        print("ERROR: Mes no tiene 31 días")
        exit()
    # Caso Error 7
    if not (dia_letra.lower().__eq__("lunes") or dia_letra.lower().__eq__("martes")
            or dia_letra.lower().__eq__("miércoles") or dia_letra.lower().__eq__("jueves")
            or dia_letra.lower().__eq__("viernes")):
        print("ERROR: dia de la semana invalido.")
        exit()

    if dia_letra.lower().__eq__("lunes") or dia_letra.lower().__eq__("martes") or dia_letra.lower().__eq__("miércoles"):
        tipo = 1
    if dia_letra.lower().__eq__("jueves"):
        tipo = 2
    if dia_letra.lower().__eq__("viernes"):
        tipo = 3

    if tipo == 1:
        if input("¿Ha Habido Examen? (Y/N)\n").lower().__eq__("y"):
            aprobados = input("Introduzca el número de aprobados:\t")
            suspensos = input("Introduzca el número de suspensos:\t")
            # Caso Error 9
            if not (aprobados.isnumeric() and suspensos.isnumeric()):
                print("ERROR: formato incorrecto.")
                exit()
            aprobados = int(aprobados)
            suspensos = int(suspensos)
            print(f"El porcentaje de aprobados es del {aprobados/(aprobados+suspensos)*100}%")

    elif tipo == 2:
        asistencia = input("Introduzca el porcentaje de asistencia:\t")
        if asistencia.find("%") < 0:

            # Caso Error 10
            if not (asistencia.isdecimal() or asistencia.isnumeric()):
                print("ERROR: formato incorrecto.")
                exit()

            asistencia = float(asistencia) * 100
        else:
            asistencia = asistencia.strip().removesuffix("%")

            # Caso Error 10
            if not (asistencia.isdecimal() or asistencia.isnumeric()):
                print("ERROR: formato incorrecto.")
                exit()
        if asistencia > 50:
            print("Asistió la mayoria.")
        else:
            print("No asistió la mayoria.")

    elif tipo == 3:
        if int(dia_num) == 1 and (int(mes) == 1 or int(mes) == 7):
            print("Comienzo de nuevo ciclo.")
        alumnos = input("Introduzca el número de alumnos:\t")
        precio = input("Introduzca el precio por alumno:\t")

        # Caso Error 11
        if not (alumnos.isnumeric() and (precio.isnumeric() or precio.isdecimal())):
            print("ERROR: formato incorrecto.")
            exit()

        alumnos = int(alumnos)
        precio = float(precio)

        print(f"El coste es igual a {round(alumnos * precio, 2)}$")


def ejer_1_while():
    """
    Ejercicio 1
    Crea una aplicación que pida un número y calcule su factorial (El factorial de un
    número es el producto de todos los enteros entre 1 y el propio número y se
    representa por el número seguido de un signo de exclamación. Por ejemplo 5! =
    1x2x3x4x5=120).
    """
    num = -1
    while num < 0:
        num = input("Introduce un número positivo:\t")
    aux = num
    fact = num
    while aux != 1:
        aux = aux - 1
        fact = fact * aux

    print(f"El factorial de {num} es: {fact}")


def ejer_2_while():
    """
    Ejercicio 2
    Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la
    suma y la media de todos los números introducidos.
    """
    num = -1
    cont = 0
    suma = 0
    while num != 0:
        num = input("Introduzca un número entero:\t")
        if num.isnumeric():
            num = int(num)
            suma = suma + num
            cont = cont + 1
        else:
            print("ERROR: Número no valido")

    print(f"La suma de los números introducidos es: {suma}\n"
          f"Su media es: {suma/cont}")


def ejer_3_while():
    """
    Ejercicio 3
    Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en
    caso contrario, el programa termina cuando se introduce un espacio
    """
    espacio = False
    while not espacio:
        letra = input("Introduzca letra")
        if letra.isspace() or len(letra) != 1:
            print("Salida de programa")
            espacio = not espacio
        else:
            letra = letra.lower()
            if (letra.__eq__("a") or letra.__eq__("e") or letra.__eq__("i")
                    or letra.__eq__("o") or letra.__eq__("u")):
                print("VOCAL")
            else:
                print("NO VOCAL")


def ejer_5_while():
    """
    Ejercicio 5
    Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra en
    el km 150, los coches tienen sentido opuesto y tienen la misma velocidad. Realizar
    un programa para determinar en qué kilómetro de esa carretera se encontrarán.
    """
    v = int(input("Introduzca Velocidad: "))
    iteracion = 0
    i = 0
    road = list([])
    road.append("o")
    while i != 150-72:
        road.append("-")
        i = i + 1
    road.append("x")
    carretera = "".join(road)
    print(carretera)
    puntero_o = v
    puntero_x = len(road) - v - 1
    while len(road)/2 > puntero_o:
        iteracion = iteracion + 1
        i = 0
        while i != puntero_o:
            i = i + 1
            road.pop(i)
            road.insert(i, "o")

        i = len(road)
        while i != puntero_x:
            i = i - 1
            road.pop(i)
            road.insert(i, "x")

        print("".join(road))
        puntero_o = puntero_o + v
        puntero_x = puntero_x - v

    print(f"Se encontraron en el km {iteracion*v + 70}")


def ejer_5_for():
    """
    Ejercicio 5
    Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
    anual y el número de años, y muestre por pantalla el capital obtenido en la
    inversión cada año que dura la inversión
    """
    inversion = float(input("Introduzca cantidad a invertir: "))
    interes = float(input("Introduzca interés anual: "))
    interes = interes / 100
    years = int(input("Introduzca el número de años: "))
    for i in range(years):
        print(f"Año número {i+1}: {round((i+1+interes) * inversion, 2)}")


def ejer_6_for():
    """
    Ejercicio 6
    Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
    una a una las letras de la palabra introducida empezando por la última.
    """
    palabra = input("Introduzca palabra:\n")
    res = ""
    for i in range(len(palabra)-1, -1, -1):
        res = res.join(palabra[i])
    print(res)


if __name__ == '__main__':
    ejer_6_for()
