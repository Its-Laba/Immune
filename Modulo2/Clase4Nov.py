"""
Clase de 4 de Noviembre
"""
import math


# Ejercicio 1:
def raiz_cubica(x):
    return x ** (1 / 3)


# Ejercicio 2:
def area_circulo(radio):
    return math.pi * radio * 2


# Ejercicio 3:
def f_c(grados):
    return (grados - 32) * (5/9)


def c_f(grados):
    return (grados * (9/5)) + 32


# Ejercicio 4:
def letra_dni(dni):
    letra = [[0, "T"], [1, "R"], [2, "W"], [3, "A"], [4, "G"], [5, "M"], [6, "Y"], [7, "F"],
             [8, "P"], [9, "D"], [10, "X"], [11, "B"], [12, "N"], [13, "J"], [14, "Z"],
             [15, "S"], [16, "Q"], [17, "V"], [18, "H"], [19, "L"], [20, "C"], [21, "K"], [22, "E"]]
    n_letra = dni % 23
    return letra[n_letra][1]


# Ejercicio 5:
def n_dias(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 366
    else:
        return 365


# Ejercicio 6:
def suma_contiguos(lista):
    suma = 0
    resta = 0
    for elem, numero in enumerate(lista):
        if elem == 0:
            resta += numero
        elif elem == len(lista)-1:
            suma += numero
        else:
            suma += numero
            resta += numero
    return suma - resta


# Ejercicio 7:
def cad_larga(lista):
    cad = ""
    for cadena in lista:
        if len(cadena) >= len(cad):
            cad = cadena
    return cad


# Ejercicio 8:
def comprueba_letra_dni(dni, letra):
    return letra_dni(dni) == letra.upper()


# Ejercicio 9:
def valor_r(i):
    return i/1200


def cuota_mensual(hipoteca, years, impuesto):
    r = valor_r(impuesto)
    m = (hipoteca * r) / (1 - (1 + r)**(-12 * years))
    return round(m, 2)


# Ejercicio 10:
def busca_inmueble(lista, precio):
    inmuebles = []
    for inmueble in lista:
        valor = precio_in(inmueble)
        print(valor)
        if valor <= precio:
            inmuebles.append(inmueble)
    return inmuebles


def precio_in(inmueble):
    year = int(inmueble.get('año'))
    metros = int(inmueble.get('metros'))
    habitaciones = int(inmueble.get('habitaciones'))
    garaje = 0
    if inmueble.get('garaje'):
        garaje = 1
    zona = inmueble.get('zona')

    antiguedad = 2022 - year
    if zona == 'A':
        return (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad / 100)
    else:
        return (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1 - antiguedad / 100) * 1.5

#
# print(busca_inmueble([{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'},
#                       {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'},
#                       {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'},
#                       {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'},
#                       {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}], 500000))


# Ejercicio 11:
def leer_fraccion():
    numerador = int(input("Introduzca el numerador: "))
    denominador = int(input("Introduzca el denominador: "))

    return simplificar_fraccion((numerador, denominador))


def intercambiar(a, b):
    if a > b:
        return a, b
    else:
        return b, a


def escribir_fraccion(func):
    num = func[0]
    den = func[1]
    if den == 1:
        print(f"{num}")
    else:
        print(f"{num}/{den}")


def calcular_mcd(a, b):
    nums = intercambiar(a, b)
    n1 = nums[0]
    n2 = nums[1]

    resto = n1 % n2
    if resto == 0:
        return n2

    return calcular_mcd(n2, resto)


def simplificar_fraccion(frac):
    num = frac[0]
    den = frac[1]
    mcd = calcular_mcd(num, den)
    while mcd != 1:
        num = num//mcd
        den = den//mcd
        mcd = calcular_mcd(num, den)
    return num, den


def sumar_fracciones(frac1, frac2):
    num1 = frac1[0]
    den1 = frac1[1]
    num2 = frac2[0]
    den2 = frac2[1]

    num = num1*den2 + num2*den1
    den = den1*den2

    return simplificar_fraccion((num, den))


def restar_fracciones(frac1, frac2):
    num1 = frac1[0]
    den1 = frac1[1]
    num2 = frac2[0]
    den2 = frac2[1]

    num = num1 * den2 - num2 * den1
    den = den1 * den2

    return simplificar_fraccion((num, den))


def mult_fracciones(frac1, frac2):
    num1 = frac1[0]
    den1 = frac1[1]
    num2 = frac2[0]
    den2 = frac2[1]

    num = num1 * num2
    den = den1 * den2

    return simplificar_fraccion((num, den))


def div_fracciones(frac1, frac2):
    num1 = frac1[0]
    den1 = frac1[1]
    num2 = frac2[0]
    den2 = frac2[1]

    num = num1 * den2
    den = den1 * num2

    return simplificar_fraccion((num, den))


def menu():
    print("MENU:")
    print("""
    OPCIONES:
    1 - Sumar 2 fracciones
    2 - Restar 2 fracciones
    3 - Multiplicar 2 fracciones
    4 - Dividir 2 fracciones
    5 - Salir
    """)
    opcion = 1
    while 0 < opcion < 5:
        opcion = int(input("Introduzca opción: "))
        if opcion == 1:
            op1()
        elif opcion == 2:
            op2()
        elif opcion == 3:
            op3()
        elif opcion == 4:
            op4()


def op1():
    frac1 = leer_fraccion()
    frac2 = leer_fraccion()
    escribir_fraccion(sumar_fracciones(frac1, frac2))


def op2():
    frac1 = leer_fraccion()
    frac2 = leer_fraccion()
    escribir_fraccion(restar_fracciones(frac1, frac2))


def op3():
    frac1 = leer_fraccion()
    frac2 = leer_fraccion()
    escribir_fraccion(mult_fracciones(frac1, frac2))


def op4():
    frac1 = leer_fraccion()
    frac2 = leer_fraccion()
    escribir_fraccion(div_fracciones(frac1, frac2))
