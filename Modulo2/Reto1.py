"""
    RETO 1 CLASE DEL 29 DE OCTUBRE
"""

import time

import Modulo2.Reto1

aplicaciones = ["Gmail", "Tinder", "Twitter", "Tiktok", "Instagram"]
passwords = ["20051206Correo!", "qwerasdf1234#", "Tw2022+LMP", "Tik2022*VTP", "Ins2022!MFR"]
last_pass = None


def show_layout():

    print("""                                                                                       
                                                                                                   
            MMMMMMMM               MMMMMMMM                                                        
            M:::::::M             M:::::::M                                                        
            M::::::::M           M::::::::M                                                        
            M:::::::::M         M:::::::::M                                                        
            M::::::::::M       M::::::::::M    eeeeeeeeeeee    nnnn  nnnnnnnn    uuuuuu    uuuuuu  
            M:::::::::::M     M:::::::::::M  ee::::::::::::ee  n:::nn::::::::nn  u::::u    u::::u  
            M:::::::M::::M   M::::M:::::::M e::::::eeeee:::::een::::::::::::::nn u::::u    u::::u  
            M::::::M M::::M M::::M M::::::Me::::::e     e:::::enn:::::::::::::::nu::::u    u::::u  
            M::::::M  M::::M::::M  M::::::Me:::::::eeeee::::::e  n:::::nnnn:::::nu::::u    u::::u  
            M::::::M   M:::::::M   M::::::Me:::::::::::::::::e   n::::n    n::::nu::::u    u::::u  
            M::::::M    M:::::M    M::::::Me::::::eeeeeeeeeee    n::::n    n::::nu::::u    u::::u  
            M::::::M     MMMMM     M::::::Me:::::::e             n::::n    n::::nu:::::uuuu:::::u  
            M::::::M               M::::::Me::::::::e            n::::n    n::::nu:::::::::::::::uu
            M::::::M               M::::::M e::::::::eeeeeeee    n::::n    n::::n u:::::::::::::::u
            M::::::M               M::::::M  ee:::::::::::::e    n::::n    n::::n  uu::::::::uu:::u
            MMMMMMMM               MMMMMMMM    eeeeeeeeeeeeee    nnnnnn    nnnnnn    uuuuuuuu  uuuu""")

    print("---------------------------------------------------------------------------------------")
    print("1. Agregar nuevas contrase??as")
    print("2. Buscar una aplicaci??n")
    print("3. Deshacer la ??ltima contrase??a")
    print("4. Modificar una contrase??a")


def main():

    show_layout()
    option = input("Introduzca opci??n deseada:\t")
    if option == "1":
        new_pass()
    elif option == "2":
        buscar_aplicacion()
    elif option == "3":
        deshacer()
    elif option == "4":
        modificar()
    else:
        "Opcion invalida."
    continuar()


def new_pass():
    nueva_app = input("Introduzca nueva aplicaci??n:\t")
    while nueva_app in aplicaciones:
        print("Aplicaci??n ya existente.")
        nueva_app = input("Introduzca nueva aplicaci??n:\t")
    nueva_pass = input("Introduzca nueva contrase??a:\t")
    while nueva_pass in passwords:
        print("Aplicaci??n ya existente.")
        nueva_pass = input("Introduzca nueva contrase??a:\t")
    for i in range(5):
        print("*     ", end="")
        time.sleep(0.2)
    print()

    aplicaciones.append(nueva_app)
    passwords.append(nueva_pass)
    Modulo2.Reto1.last_pass = nueva_pass
    print("Operaci??n Realizada con exito.")


def buscar_aplicacion():
    nueva_app = input("Introduzca aplicaci??n:\t")
    while nueva_app not in aplicaciones:
        print("Aplicaci??n no encontrada.")
        nueva_app = input("Introduzca otra aplicaci??n:\t")

    print(f"Contrase??a de la aplicaci??n {nueva_app} es {passwords[aplicaciones.index(nueva_app)]}")


def deshacer():
    if Modulo2.Reto1.last_pass is None:
        print("No ha insertado ninguna contrase??a nueva.")
    else:
        index = passwords.index(Modulo2.Reto1.last_pass)
        passwords.remove(Modulo2.Reto1.last_pass)
        aplicaciones.remove(aplicaciones[index])
        for i in range(5):
            print("*     ", end="")
            time.sleep(0.2)
        print()
        print("Operaci??n Realizada con exito.")


def modificar():
    app = input("Introduzca aplicaci??n a modificar su contrase??a:\t")
    while app not in aplicaciones:
        print("Aplicaci??n no encontrada.")
        app = input("Introduzca otra aplicaci??n:\t")
    new_pass = input("Introduzca nueva contrase??a:\t")
    index = aplicaciones.index(app)
    passwords.remove(passwords[index])
    passwords.insert(index, new_pass)
    for i in range(5):
        print("*     ", end="")
        time.sleep(0.2)
    print()
    print("Operaci??n Realizada con exito.")
    Modulo2.Reto1.last_pass = new_pass


def continuar():
    cont = input("??Desea continuar? (Y/N)\n")
    if cont.upper() != "N":
        main()
    else:
        print("Gracias por utilizar nuestra app.")


if __name__ == '__main__':
    main()
