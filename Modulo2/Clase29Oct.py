"""
    Ejercicios vistos en la clase del 29 de Octubre
"""


def ejer_1():
    """
    Ejercicio 1
    Escribir un programa que almacene las asignaturas de un curso (por ejemplo
    Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por
    pantalla.
    """
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    for i in asignaturas:
        print(i)

def ejer_2():
    """
    Ejercicio 2
    Escribir un programa que almacene en una lista los números del 1 al 10 y los
    muestre por pantalla en orden inverso separados por espacios.
    """
    lista_num = list(range(1, 11))
    lista_num.reverse()
    for num in lista_num:
        print(num, end=" ")

def ejer_3():
    """
    Ejercicio 3
    Escribir un programa que pida al usuario una palabra y muestre por pantalla el
    número de veces que contiene cada vocal.
"""
    palabra = input("Introduzca una palabra:\t")
    vocal = ["a", "e", "i", "o", "u"]
    cont = 0
    for i in palabra:
        if i in vocal:
            cont += 1
    print(f"La palabra {palabra} tiene {cont} vocales")


def ejer_4():
    """
    Ejercicio 4
    Escribir un programa que almacene las asignaturas de un curso (por ejemplo
    Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
    nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
    aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
    usuario tiene que repetir.
    """
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    suspensas = []
    for i in asignaturas:
        nota = float(input(f"Nota sacada en {i}:\t"))
        if not nota >= 5:
            suspensas.append(i)
    print("Tiene que repetir: ")
    for i in suspensas:
        print(i)


def ejer_5():
    """
    Ejercicio 5
    Escribir un programa que pregunte al usuario los números ganadores de la lotería
    primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
    a mayor.
    """
    num_ganadores = []
    for i in range(5):
        num = int(input(f"Introduzca numero {i+1} ganador:\t"))
        num_ganadores.append(num)
    num_ganadores.sort(reverse=True)
    print(num_ganadores)


def ejer_6():
    """
    Ejercicio 6
    Escribir un programa que guarde en un diccionario los precios de las frutas de la
    tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla
    el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe
    mostrar un mensaje informando de ello.
    """
    fruta = {
        "Platano": 1.35,
        "Manzana": 0.8,
        "Pera": 0.85,
        "Naranja": 0.7
    }
    fruta_user = input("Introduzca Fruta:\t")
    if fruta_user.title() in fruta:
        kilos = float(input("Introduzca Kilos:\t"))
        print(f"{kilos}kg de {fruta_user} son {fruta.get(fruta_user.title()) * kilos}")
    else:
        print("Fruta no valida.")


def ejer_7():
    """
    Ejercicio 7
    Escribir un programa que cree un diccionario simulando una cesta de la compra. El
    programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta
    que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la
    compra y el coste total, con el siguiente formato:
    """
    catalogo = {}
    articulo = input("Introduzca nombre del artículo a añadir: (FIN para finalizar)\t")
    while not articulo.upper().__eq__("FIN"):
        precio = float(input(f"Introduzca precio del artículo {articulo}:\t"))
        catalogo.update({articulo: precio})
        articulo = input("Introduzca nombre del artículo a añadir: (FIN para finalizar)\t")

    print("Lista de la compra:", end="\t")
    print(*catalogo.keys(), sep=", ")

    print("Coste Total:\t", sum(catalogo.values()))


if __name__ == '__main__':
    ejer_7()
