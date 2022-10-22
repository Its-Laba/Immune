"""
Archivo de los ejercicios de la clase del 22 de Octubre
"""


def ejer_1():
    """
    Ejercicio 1:
    Escribir un programa que muestre por pantalla la cadena¡Hola Mundo!.
    """
    print("¡Hola Mundo!")


def ejer_2():
    """
    Ejercicio 2
    Escribir un programa que almacene la cadena ¡HolaMundo! en una variable y
    luego muestre por pantalla el contenido de la variable
    """
    hola = "¡Hola Mundo!"
    print(hola)


def ejer_3():
    """
    Ejercicio 3:
    Escribir un programa que pregunte el nombre del usuario en la consola y después
    de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola<nombre>!,
    donde<nombre>es el nombre que el usuario haya introducido.
    """
    nombre = input("Introduzca nombre: ")
    print(f"¡Hola {nombre}!")


def ejer_4():
    """
    Ejercicio 4
    Escribir un programa que muestre por pantalla el resultado de la siguiente
    operación aritmética
    """
    op = "((3+2)/2*5)**2"
    print(op)


def ejer_5():
    """
    Ejercicio 5
    Escribir un programa que pregunte al usuario por el número de horas trabajadas y
    el coste por hora. Después debe mostrar por pantalla la paga que le corresponde
    """
    horas = input("Introduzca horas trabajadas: ")
    coste = int(input("Introduzca coste de la hora: "))
    print(f"Le corresponde al trabajador una paga de {coste*horas} euros")


def ejer_6():
    """
    Ejercicio 6
    Escribir un programa que lea un entero positivo, n, introducido por el usuario y
    después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma
    de losnprimeros enteros positivos puede ser calculadade la siguiente forma: n(n+1)/2
    """
    n = int(input("Introduzca n: "))
    print(f"La suma de todos los numeros hasta {n} es: {n*(n+1)//2}")


def ejer_7():
    """
    Ejercicio 7
    Escribir un programa que pida al usuario su peso(en kg) y estatura (en metros),
    calcule el índice de masa corporal y lo almacene en una variable, y muestre por
    pantalla la frase Tu índice de masa corporal es <imc> donde <imc> es el índice de
    masa corporal calculado redondeado con dos decimales.
    Fórmula: peso (kg) / [estatura (m)]2
    """
    peso = float(input("Introduzca su peso (en kg): "))
    estatura = float(input("Introduzca su altura (en metros): "))
    print(f"Tu índice de masa corporal es {peso/estatura**2}")


def ejer_8():
    """
    Ejercicio 8
    Escribir un programa que pida al usuario dos números enteros y muestre por
    pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde <n> y <m> son los
    números introducidos por el usuario, y <c> y <r> son el cociente y el resto de la
    división entera respectivamente.
    """
    n = int(input("Introduzca el número n: "))
    m = int(input("Introduzca el número m: "))
    c = n//m
    r = n%m
    print(f"{n}/{m} = {c} con resto {r}")

if __name__ == '__main__':
    Ejer8()