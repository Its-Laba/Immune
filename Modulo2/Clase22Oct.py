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
    horas = int(input("Introduzca horas trabajadas: "))
    coste = float(input("Introduzca coste de la hora: "))
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
    print(f"Tu índice de masa corporal es {round(peso/estatura**2,2)}")


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


def ejer_1_2():
    """
    Ejercicio 1
    Escribir un programa que pregunte el nombre del usuario en la consola y después
    de que el usuario lo introduzca muestre por pantalla el mensaje: <NOMBRE> tiene
    <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el
    número de letras que tienen el nombre
    """
    nombre = input("Introduzca su nombre: ")
    print(f"{nombre} tiene {len(nombre)} letras")


def ejer_2_2():
    """
    Ejercicio 2
    Los teléfonos de una empresa tienen el siguiente formato
    prefijo-número-extensión donde el prefijo es el código del país +34, y la
    extensión tiene dos dígitos (por ejemplo +34-913724710-56).
    Escribir un programa que pregunte por un número de teléfono con este formato en la consola y muestre
    por pantalla el número de teléfono sin el prefijo y la extensión.
    """
    telefono = input("Introduzca número de telefono en el formato de la empresa: ")
    print(f"El número de telefono sin prefijo y extensión es: {telefono[4:-3]}")


def ejer_3_2():
    """
    Ejercicio 3
    Escribir un programa que pida al usuario que introduzca una frase en la consola y
    una vocal en minúscula, y después muestre por pantalla la misma frase pero con la
    vocal introducida en mayúscula.
    :return:
    """
    frase = input("Introduzca una frase: ")
    vocal = input("Introduzca una vocal en minúscula: ")
    frase_mayuscula = frase.replace(vocal, vocal.upper())
    print(frase_mayuscula)


def ejer_4_2():
    """
    Ejercicio 4
    Escribir un programa que pregunte el nombre completo del usuario en la consola y
    después muestre por pantalla el nombre completo del usuario tres veces, una con
    todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la
    primera letra del nombre y de los apellidos en mayúscula.El usuario puede
    introducir su nombre combinando mayúsculas y minúsculas como quiera.
    :return:
    """
    nombre_completo = input("Introduzca su nombre completo: ")
    print(nombre_completo.lower())
    print(nombre_completo.upper())
    print(nombre_completo.capitalize())


def ejer_5_2():
    """
    Ejercicio 5
    Escribir un programa que pregunte al usuario una cantidad a invertir, el interés
    anual y el número de años, y muestre por pantalla el capital obtenido en la
    inversión.
    :return:
    """
    inversion = float(input("Introduzca la cantidad a invertir: "))
    interes = float(input("Introduzca el interés anual (en porcentaje): "))
    years = int(input("Introduzca número de años: "))
    ganancias = inversion * interes/100 * years
    print(f"Has obtenido {ganancias}$ de su inversión.")


def ejer_6_2():
    """
    Ejercicio 6
    Una juguetería tiene mucho éxito en dos de sus productos: payasos ym uñecas.
    Suele hacer venta por correo y la empresa de logística les cobra por peso de cada
    paquete asíque deben calcular el peso de los payasos y muñecas que saldrán en
    cada paquete a demanda. Cada payaso pesa 112g y cada muñeca 75g.
    Escribe un programa que lea el número de payasos y muñecas vendidos en el último pedido y
    calcule el peso total del paquete que será enviado.
    :return:
    """
    n_payasos = int(input("Introduzca el número de payasos vendidos: "))
    n_dolls = int(input("Introduzca el número de muñecas vendidos: "))
    peso = n_payasos * 112 + n_dolls * 75
    print(f"El peso del paquete será de {peso}g.")


def ejer_7_2():
    """
    Ejercicio 7
    Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de
    interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de
    año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa
    que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros,
    introducida por el usuario. Después el programa debe calcular y mostrar por
    pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear
    cada cantidad a dos decimales.
    :return:
    """
    dinero_ahorros = float(input("Introduzca cantidad de dinero que quiere depositar en la cuenta de ahorros: "))
    dinero_ahorros_1 = dinero_ahorros * 1.04
    print(f"Dinero en la cuenta de ahorro tras 1 año: {round(dinero_ahorros_1,2)}")
    dinero_ahorros_2 = dinero_ahorros_1 * 1.04
    print(f"Dinero en la cuenta de ahorro tras 2 años: {round(dinero_ahorros_2,2)}")
    dinero_ahorros_3 = dinero_ahorros_2 * 1.04
    print(f"Dinero en la cuenta de ahorro tras 3 años: {round(dinero_ahorros_3,2)}")


def ejer_8_2():
    """
    Ejercicio 8
    Una panadería vende barras de pan a 3.49€ cada una. El pan que no es del día tiene
    un descuento del 60%. Escribir un programa que comience leyendo el número de
    barras vendidas que no son del día. Después el programa debe mostrar el precio
    habitual de una barra de pan, el descuento que se le hace por no ser fresca y el
    coste final total
    :return:
    """
    n_pan_nodia = int(input("Introduzca el número de panes que no son del dia vendidos: "))
    valor = n_pan_nodia * 3.49
    descuento = valor * 0.6
    print(f"{valor} - {descuento} = {valor * 0.6}")


def ejer_9_2():
    """
    Ejercicio 9
    Escriba un programa que solicite al usuario el ingreso de un texto y almacene ese
    texto en una variable. A continuación, mostrar en pantalla la primera letra del texto
    ingresado. Luego, solicitar al usuario que ingrese un número positivo menor a la
    cantidad de caracteres que tiene el texto que ingresó ( por ejemplo, si escribió la
    palabra “HOLA”, tendrá que ser un número entre 0 y 4 ) y almacenar este número en
    una variable llamada índice.
    Mostrar en pantalla el carácter del texto ubicado en la posición dada por índice.
    :return:
    """
    texto = input("Introduzca un texto: ")
    index = int(input(f"Introduzca un entero positivo menor que {len(texto)}: "))
    print(f"La letra en la posición {index} es: {texto[index]}")


def ejer_10_2():
    """
    Ejercicio 10
    Escriba un programa que le solicite al usuario ingresar una fecha formada por 8
    números, donde los primeros dos representan el día, los siguientes dos el mes y los
    últimos cuatro el año (DDMMAAAA). Este dato debe guardarse en una variable con
    tipo int(númeroentero). Finalmente, mostrar al usuario la fecha con el formato
    DD / MM / AAAA
    :return:
    """
    date = int(input("Introduzca la fecha en el formato (DDMMAAAA): "))
    fecha = str(date)
    dia = fecha[:2]
    mes = fecha[2:4]
    year = fecha[4:]
    print(f"{dia} / {mes} / {year}")


def ejer_11_2():
    """
    Ejercicio 11
    Escriba un programa que solicite al usuario el ingreso de una temperatura en escala
    Fahrenheit (debe permitir decimales) y le muestre el equivalente en grados Celsius.
    :return:
    """
    faherenheit = float(input("Introduzca los grados en Fahrenheit: "))
    celsius = (5/9) * (faherenheit - 32)
    print(f"{faherenheit}ºF = {celsius}ºC")


if __name__ == '__main__':
    ejer_10_2()
