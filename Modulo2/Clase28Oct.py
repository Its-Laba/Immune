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

    if not (dia_letra.isalnum() and dia_num.isnumeric() and mes.isnumeric()):
        print("El formato no es valido debe ser: <[alfanumérico], [numérico]/[numérico]>.")
        exit()

    if int(dia_num) < 0 or int(mes) < 0:
        print("la fecha no puede ser negativa.")
        exit()

    if int(dia_num) > 31:
        print("ERROR: El día no puede exceder de 31.")
        exit()

    if int(mes) > 12:
        print("ERROR: El mes no puede exceder de 12.")
        exit()

    if not (dia_letra.lower().__eq__("lunes") or dia_letra.lower().__eq__("martes")
            or dia_letra.lower().__eq__("miércoles") or dia_letra.lower().__eq__("jueves")
            or dia_letra.lower().__eq__("viernes")):
        print("ERROR: dia de la semana invalido.")
        exit()

    tipo = input("Introduzca tipo de clase:\n"
                 "1. Inicial \n"
                 "2. Intermedio\n"
                 "3. Avanzado\n"
                 "4. Práctica Hablada\n"
                 "5. Inglés Para Viajeros\n")

    if int(tipo) < 4:
        if input("¿Ha Habido Examen? (Y/N)\n").lower().__eq__("y"):
            aprobados = int(input("Introduzca el número de aprobados:\t"))
            suspensos = int(input("Introduzca el número de suspensos:\t"))
            print(f"El porcentaje de aprobados es del {aprobados/(aprobados+suspensos)*100}%")

    elif int(tipo) == 4:
        asistencia = input("Introduzca el porcentaje de asistencia:\t")
        if asistencia.find("%") < 0:
            asistencia = float(asistencia) * 100
        else:
            asistencia = float(asistencia.strip().removesuffix("%"))
        if asistencia > 50:
            print("Asistió la mayoria.")
        else:
            print("No asistió la mayoria.")

    elif int(tipo) == 5:
        if int(dia_num) == 1 and (int(mes) == 1 or int(mes) == 7):
            print("Comienzo de nuevo ciclo.")
        alumnos = int(input("Introduzca el número de alumnos:\t"))
        precio = float(input("Introduzca el precio por alumno:\t"))

        print(f"El coste es igual a {round(alumnos * precio, 2)}$")


if __name__ == '__main__':
    reto_if()
