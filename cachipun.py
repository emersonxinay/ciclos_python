# importamos libreria
import sys
# libreria random es para sacar numeros aleatorios
import random

# variable para seguir o terminar el juego
continuar = True
# el ciclo para continuar el juego
while continuar:
    # declaramos la variable para seleccionar la jugada o salir
    jugador = input('''
===============================================
            JUGAR CACHIPUN
===============================================
        SELECCIONA UNA OPCIÓN
===============================================

Piedra.
Papel.
Tijera.
Salir.

Seleccione la opcion que desea: ''').lower()
    # la condición si ingrese diferente a las opciones del juego
    if (jugador != 'piedra' and jugador != 'papel' and jugador != 'tijera' and jugador != 'salir'):
        print('Argumento inválido: Debe ser piedra, papel o tijera.')
    # la condición para terminar el juego
    elif jugador == 'salir':
        print("Saliendo...del juego")
        continuar = False
    # si en caso ingresa dato valido
    else:
        # el metodo que nos va dar valor aleatorio entre la lista para la jugada del computador
        computador = random.choice(['piedra', 'papel', 'tijera'])

        print(f'''
        Tu jugaste {jugador}.
        Computador jugó  {computador}''')
        # evaluamos todas las condiciones para que ganes
        if (jugador == 'piedra' and computador == 'tijera') or (jugador == 'tijera' and computador == 'papel') or (jugador == 'papel' and computador == 'piedra'):
            print('Felicitaciones has ganado!!!')
        # empatar
        elif jugador == computador:
            print('Empate!!')
        # perder el juego contra el computador
        else:
            print('Perdiste :(')
            continuar = True

        # Si quiere volver a jugar
        if jugador != "salir":
            resp = input(
                '¿Desea volver al menu? si Es así Escribe Y o y , o si desear salir escribe "salir" :  ')
            if resp == 'Y' or resp == 'y':
                pass
            elif resp != "salir":
                print("ingrese una opción correcta: ")
            else:
                print("Saliendo...del juego cachipun")
                continuar = False
