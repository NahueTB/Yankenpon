#! /usr/bin/env python3

import random


def jugarDeNuevo():
    rta = input('Querés jugar de nuevo? (S/N): ').lower()
    if rta == 's':
        return True
    elif rta == 'n':
        return False
    elif len(rta) > 1:
        print('Tu respuesta debe ser "S" o "N" ')
        jugarDeNuevo()
    else: 
        print('Disculpá, no entendí tu rta. \nTu respuesta debe ser "S" o "N" ')
        jugarDeNuevo()


yankenpon = ['Piedra', 'Papel', 'Tijera']

jugar = True

while jugar == True:
    pc = yankenpon[random.randint(0,2)]

    eleccion = int(input('Elegí: "Piedra"(1), "Papel"(2) o "Tijera"(3). '))

    if eleccion > 3:
        print('Tenés que elegir un numero del 1 al 3.\n')
        eleccion = input('Elegí: "Piedra"(1), "Papel"(2) o "Tijera"(3). ')
    
    jugador = yankenpon[eleccion-1]
    
    if jugador == pc:
        print(f'Vos: {jugador} | PC: {pc} | Es un empate.')
    elif jugador == yankenpon[0] and pc == yankenpon[1]:
        print(f'Vos: {jugador} | PC: {pc} | Ganó la compu!')
    elif jugador == yankenpon[1] and pc == yankenpon[2]:
        print(f'Vos: {jugador} | PC: {pc} | Ganó la compu!')
    elif jugador == yankenpon[2] and pc == yankenpon[0]:
        print(f'Vos: {jugador} | PC: {pc} | Ganó la compu!')
    elif jugador == yankenpon[2] and pc == yankenpon[1]:
        print(f'Vos: {jugador} | PC: {pc} | Ganaste!')
    elif jugador == yankenpon[1] and pc == yankenpon[0]:
        print(f'Vos: {jugador} | PC: {pc} | Ganaste!')
    elif jugador == yankenpon[0] and pc == yankenpon[2]:
        print(f'Vos: {jugador} | PC: {pc} | Ganaste!')
    jugar = jugarDeNuevo()

print('Gracias por jugar. Nos vemos la proxima!')