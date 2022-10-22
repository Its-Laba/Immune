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


if __name__ == '__main__':
    pass
