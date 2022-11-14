# MENU
saldo = 100000

continuar = True
while continuar:
    menu = int(input('''\n
===============================================
Cajero Automatico
===============================================

1.- Ingresar dinero.
2.- Retirar dinero.
3.- Mostrar saldo.
4.- Salir

Seleccione la opcion que desea: '''))
    if menu == str:
        print("Ingrese un numero de la opción: ")
    else:

        # DEPOSITAR
        if menu == 1:
            x = int(input("\nCuanto dinero desea ingresar: $"))
            saldo = saldo + x
            print(f"Su saldo queda en ${saldo}.")

        # RETIRAR
        elif menu == 2:
            x = int(input("\nCuanto dinero desea retirar: $"))
            if x % 5000 == 0:
                if x == 0:
                    print("No puede retirar $0.")
                elif x > saldo or x < 0:
                    print(
                        f"Ingrese un retiro valido, su saldo es de ${saldo}.")
                elif x <= saldo or x > 0:
                    saldo -= x
                    print(f"Usted ha retirado: ${x}.")
                    print(f"Su saldo queda en ${saldo}.")
            else:
                print("Este cajero solo entrega billetes multiplos de 5.")

        # SALDO
        elif menu == 3:
            print(f"\nSu saldo es de: ${saldo}.")

        # SALIR
        elif menu == 4:
            print("\nGracias por usar este cajero.")
            continuar = False

        # OTROS
        else:
            print("\nOpcion no encontrada.")

        # Si quiere volver
        if menu != 4:
            resp = input(
                '¿Desea volverl al menu? si Es así Escribe Y o y , o si desear salir escribe "salir" ')
            if resp == 'Y' or resp == 'y':
                pass
            else:
                continuar = False
