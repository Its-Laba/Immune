"""
    Ejercios ficheros Clase de 5 de Noviembre
"""


def ejer1():
    f = open("./Files/Ejercicio1.txt", "w+")
    f.write("Este es el ejercicio 1\n")
    f.close()


def ejer2():
    f = open("./Files/Ejercicio1.txt", "r")
    print(f"Estado: {f.closed}, Modo: {f.mode}, Nombre: {f.name}, Encode: {f.encoding}")
    f.close()


def ejer3():

    n = 11
    while not 0 < n < 11:
        n = int(input("Introduce numero del 1 al 10:\t"))
    f = open(f"./Files/tabla-{n}.txt", "w+")
    for i in range(10):
        f.write(str(n)+f"* {i+1} = {(i+1)*n}\n")
    f.close()


def ejer4():
    empleados = []
    f = open("./Files/Ejercicio4.txt", "r")
    lineas = f.readlines()
    f.close()
    for linea in lineas:
        linea = linea[:-1]
        valores = linea.split(";")
        empleados.append({"id": valores[0], "nombre": valores[1], "apellido": valores[2], "nacimiento": valores[3]})
    print(*empleados, sep="\n")


def ejer5():
    f = open("./Files/primos.txt", "w+")
    lista = list(range(2, 100))
    for n in lista:
        prime = True
        for i in range(2, n):
            if n % i == 0:
                prime = False
        if prime:
            f.write(str(n)+"\n")
    f.close()


def ejer6():
    ejer3()
    m = 11
    while not 0 < m < 11:
        m = int(input("Introduzca un numero del 1 al 10:\t"))
    f = open(f"./Files/tabla-n.txt")
    lista = f.readlines()
    print(lista[m-1][:-1])


def ejer7():
    productos = ("Nike Air Max 90", "Nike Air Force 1", "Nike Blazer Mid 77",
                 "Air Jordan 1 Mid", "Nike SB Shane", "Nike Waffle One SE", "Nike Air Presto",
                 "Nike React Vision")
    precios = (139.99, 99.99, 109.99, 129.99, 74.99, 109.89, 85.99, 119.80)
    stocks = (43, 1, 0, 32, 105, 12, 50, 6)

    f = open("./Files/ticket.txt", "w")
    for i in range(1, len(productos)):
        print(f"{i}. {productos[i]}")
    cad = input("Introduce número de la zapatilla deseada: (* para salir)  ")
    carrito = []
    while cad != "*":
        carrito.append(cad)
        cad = input("Introduce número de la zapatilla deseada: (* para salir)  ")
    coste = 0
    for zapa in carrito:
        f.write(productos[int(zapa)-1]+"\n")
        coste += precios[int(zapa)-1]
    f.write(f"Coste Total: {coste}")
    f.close()


def ejer8():
    f = open("./Files/texto.txt", "r")
    lista = f.readlines()
    maximo = max(lista, key=len)
    print(maximo)
    f.close()


def ejer10(tipo):
    import os

    if not os.path.isfile("./Files/contador.txt"):
        f = open("./Files/contador.txt", "w")
        f.write("0")
        f.close()
    f = open("./Files/contador.txt", "r")
    cont = int(f.read())
    f.close()
    if tipo.lower() == "inc":
        cont += 1
    elif tipo.lower() == "dec":
        cont -= 1
    else:
        print("Cont: ", cont)
    f = open("./Files/contador.txt", "w")
    f.write(str(cont))
    f.close()


