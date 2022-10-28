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
    if hombre.__eq__("M"):
        hombre = True
    else:
        hombre = False

    letra = ord(nombre.strip()[0].upper())
    if (hombre and letra > 78) or (not hombre and letra < 77):
        print("Pertenece al grupo A")
    else:
        print("Pertenece al grupo B")


if __name__ == '__main__':
    ejer_6()
