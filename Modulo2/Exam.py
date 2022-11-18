"""     Examen del 18 de Noviembre     """


def ejercicio_1():
    """
    Ejercicio 1 del examen.
    Dada la lista marcas [marcas de ropa]y la lista satisfaccion [ranking de estrellas de satisfaccion].
    Hacer un programa que añada una marca y la satisfacción. ¡Las marcas no pueden repetirse!
    """

    marcas = ["Primark", "Zara", "Mango", "El Ganso", "Scalpers", "Bershka", "Pull&Bear", "H&M"]
    satisfaccion = ["*", "***", "****", "***", "*****", "**", "***", "**"]

    salir = False
    while not salir:
        for index, marca in enumerate(marcas, start=1):
            print(f"{index}. {marca}")
        nueva_marca = input("Introduzca nueva marca a insertar: (Salir para cerrar programa) ")
        if nueva_marca.title().__eq__("Salir"):
            # Salida del programa
            salir = True
            continue
        if nueva_marca.title() in marcas:
            print("La marca ya está registrada. Introduzca otra.")
        else:
            estrellas = input("Introduzca el rating de la nueva marca: ")
            while estrellas.count("*") != len(estrellas):
                # Comprobación de que solo se introduzcan asteriscos
                print("Debe insertar el rating en formato de estrella. Ej) **")
                estrellas = input("Introduzca el rating de la nueva marca: ")
            marcas.append(nueva_marca.title())
            satisfaccion.append(estrellas)


def ejercicio_2():
    """
    Ejercicio 2 del examen.
    Dada la lista marcas [[marca, rating]]. Desarrolla un programa en el que muestre un menu:
    1 - Modificar puntuación
    2 - Eliminar marca
    3 - Salir
    E implementar cada opción del menu
    """

    marcas = [["Primark", "*"], ["Zara", "***"], ["Mango", "****"], ["El Ganso", "***"], ["Scalpers", "*****"],
              ["Bershka", "**"], ["Pull & Bear", "***"], ["H&M", "**"]]

    salir = False
    while not salir:
        print("""
        1 – Modificar puntuación
        2 – Eliminar marca
        3 - Salir
        """)

        try:
            opcion = int(input("Selecciona la opción: "))
            if opcion < 1 or opcion > 3:
                raise ValueError
        except ValueError:
            print("La opcion debe ser un número entero en 1-3")

        else:
            if opcion == 3:
                # Salida del programa
                salir = True
                continue

            if opcion == 1:

                modificar = input("Introduzca la marca a modificar: ")
                pos = None  # Crear una variable para la posicion de la marca
                estrellas = ""

                for index, marca in enumerate(marcas, start=1):
                    if modificar.title() in marca[0]:
                        estrellas = input(f"Introduzca el nuevo rating de {modificar}: ")
                        while estrellas.count("*") != len(estrellas):
                            # Comprobación de que solo se introduzcan asteriscos
                            print("Debe insertar el rating en formato de estrella. Ej) **")
                            estrellas = input(f"Introduzca el nuevo rating de {modificar}: ")
                        pos = index

                if pos is None:  # Comprobación de que esta en la lista.
                    print(modificar.title(), "no esta en la base de datos.")
                else:
                    marcas.insert(pos, [modificar.title(), estrellas])

            if opcion == 2:

                for index, marca in enumerate(marcas, start=1):
                    print(f"{index}. {marca[0]}")

                try:
                    eliminar = int(input("Selecciona la marca a eliminar: "))
                    if eliminar < 0 or eliminar > len(marcas):
                        raise ValueError
                except ValueError:
                    print("Debe introducir el número correspondiente a la marca que desea eliminar.")

                else:
                    pos_elim = eliminar - 1
                    marcas.pop(pos_elim)


def ejercicio_3():
    """
    Ejercicio 3 del examen
    Dadas las listas marcas [[marca, dueño, ingresos]] y emp_propietarias [].
    Escriba una función que muestre por pantalla las empresas propietarias. El usuario introducirá una de ellas y se
    mostrara el sumario de ventas globales de las marcas además fuera de la función aquellas marcas de que tenga una
    media de ventas mensuales (individualmente) superior a 1 millón de euros
    """
    emp_propietarias = ["Mango", "Inditex", "Tendam", "Pepe Jeans"]
    marcas = [["HE", "Mango", 9958500],
              ["Zara", "Inditex", 87550000],
              ["Mango", "Mango", 6542000],
              ["Violeta", "Mango", 1558000],
              ["Cortefiel", "Tendam", 3258600],
              ["Bershka", "Inditex", 78900000],
              ["Pull&Bear", "Inditex", 7540000],
              ["Springfield", "Tendam", 124990000],
              ["Massimo Dutti", "Inditex", 5490000],
              ["Pepe Jeans", "Pepe Jeans", 3459080],
              ["Hackett", "Pepe Jeans", 6872000],
              ["Pedro del Hierro", "Tendam", 8356000]]

    def sumario_ventas(emp):
        """
        Función que muestra por pantalla el sumario de venta globales de las marcas de emp
        :param emp: Nombre de la empresa propietaria.
        """
        sum = 0
        for marca in marcas:
            if emp in marca[1]:
                sum += marca[2]/12
        print(f"La media mensual de venta de la marca seleccionada es: {round(sum, 2)} euros.")

    for index, emp in enumerate(emp_propietarias, start=1):
        print(f"{index}. {emp}")

    try:
        opcion = int(input("Seleccione la empresa propietaria de la que quiere información > "))
        if opcion < 0 or opcion >= len(emp_propietarias):
            raise ValueError
    except ValueError:
        print("Debe insertar el número correspondiente a la marca deseada.")

    else:
        empresa = emp_propietarias[opcion-1]
        sumario_ventas(empresa)
        # Fuera de la funcion
        marca_millon = []  # Almacenamos marca, ganancia mensual
        for marca in marcas:
            if empresa in marca[1]:
                mes = marca[2]/12
                if mes > 1_000_000:
                    marca_millon.append([marca[0], mes])
        if len(marca_millon) != 0:  # Si no esta vacia se printea
            print("Las marcas que superan el millón de euros mensuales son:")
            for marca in marca_millon:
                print(marca[0], " - ", round(marca[1], 2))


def ejercicio_4():
    """
    Ejercicio 4 del examen.
    Dado un fichero mostrarlo por pantalla con el formato pedido.
    """
    f = open("marcas.txt", "r")
    lineas = f.readlines()
    f.close()
    for linea in lineas:
        marca = linea.split(",")
        if marca[2][-1] == "\n":
            marca[2] = marca[2][:-1]
        print(marca[0])
        print("-----------------------")
        print(f"Empresa Propietaria: {marca[1]}")
        print(f"Ventas Globales: {marca[2]} euros\n")


if __name__ == "__main__":
    ejercicio_4()
