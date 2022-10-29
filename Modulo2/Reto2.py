"""
    RETO 2 DE LA CLASE DEL 29 DE OCTUBRE
"""

code = list("MURCIELAGO")


def menu():
    print("MENU")
    print("-.-.-.-.-.-.-.-.-")
    print("OPCIONES:")
    print("1. Encriptar")
    print("2. Desencriptar")


def main():
    menu()
    option = input("Introduzca opcion:\t")
    if option == "1":
        encript()
    elif option == "2":
        decript()
    else:
        print("Opcion no valida.")
    continuar()


def encript():
    mensaje = list(input("Frase a encriptar: "))
    for letra in mensaje:
        if letra.upper() in code:
            mensaje[mensaje.index(letra)] = code.index(letra.upper())
    print("Frase encriptada: ", end="")
    print(*mensaje, sep="")
    print()


def decript():
    mensaje = list(input("Frase a desencriptar: "))
    for letra in mensaje:
        if letra.isnumeric():
            mensaje[mensaje.index(letra)] = code[int(letra)]
    print("Frase desencriptada: ", end="")
    print(*mensaje, sep="")
    print()


def continuar():
    cont = input("¿Desea continuar? (Y/N)\n")
    if cont.upper() != "N":
        main()
    else:
        print("Gracias por utilizar nuestra app.")


if __name__ == '__main__':
    main()
