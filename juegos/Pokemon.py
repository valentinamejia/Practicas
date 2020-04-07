import random

def tirar_dado(num):
    return random.randint(1,num)

class Pokemon:
    def __init__(self, nombre, ataque):
        self.nombre = nombre
        self.ataque = ataque
        self.vida = 100

    def gano(self):
        print(f'{self.nombre} gano esta batalla en {ronda} rondas')
        print('suerte en la proxima ')

p1 = Pokemon('pikachu', 15)
p2 = Pokemon('Charmander', 12)
p3 = Pokemon('Bulbasaur', 13)
p4 = Pokemon('Squirtle', 16)
p5 = Pokemon('Slowbro', 14)


while True:

    print('''Elige tu pokemon:
                    (1) Pikachu
                    (2) Charmander
                    (3) Bulbasaur
                    (4) Squirtle
                    (5) Slowbro
                    ''')
    jugador1 = input('Jugador1: ')
    jugador2 = input('jugador2: ')

    if jugador1 == '1':
        jugador1 = p1
    if jugador1 == '2':
        jugador1 = p2
    if jugador1 == '3':
        jugador1 = p3
    if jugador1 == '4':
        jugador1 = p4
    if jugador1 == '5':
        jugador1 = p5

    if jugador2 == '1':
        jugador2 = p1
    if jugador2 == '2':
        jugador2 = p2
    if jugador2 == '3':
        jugador2 = p3
    if jugador2 == '4':
        jugador2 = p4
    if jugador2 == '5':
        jugador2 = p5

    if jugador1 == jugador2:
        print('no pueden jugar con el mismo personaje, intenten nuevamente')

    if jugador1 != jugador2:
        turno = tirar_dado(2)
        ronda = 1

        print('Ha iniciado la batalla')
        print(f'{jugador1.nombre} se enfrenta a {jugador2.nombre}\n')

        while jugador1.vida > 0 and jugador2.vida > 0:
            print((f'\n======== {ronda} RONDA =========='))
            if turno == 1:
                jugador2.vida = jugador2.vida - jugador1.ataque
                turno = 2
                print(f'{jugador1.nombre} ataca, {jugador2.nombre} ahora tiene {jugador2.vida} de vida\n')
            else:
                jugador1.vida = jugador1.vida - jugador2.ataque
                turno = 1
                print(f'{jugador2.nombre} ataca, {jugador1.nombre} ahora tiene {jugador1.vida} de vida\n')
            ronda += 1

        if jugador1.vida <= 0:
            jugador2.gano()
        else:
            jugador1.gano()


    opcion = input('''\n Ingresa (1) volver a jugar o (2) para salir del programa: 
     >''')
    if opcion == '2':
        break
    if opcion == '1':
        print('---------o--------\n')








