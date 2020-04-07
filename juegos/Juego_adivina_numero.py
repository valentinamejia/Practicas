#------------------------ Juego adivina el número----------------

def adivina():
    import random

    adivina = random.randint(1, 10)

    print('Hola, cómo te llamas?')
    nombre = input()

    print(f'Muy bien {nombre} estoy pensando en un número entre 1 y 10, intenta adivinarlo, tienes 3 intentos')

    num = int(input('\nintenta adivinarlo: '))

    if num == adivina:
        print("ganaste!")
    else:
        if num > adivina:
            print('Intenta un número más pequeño')
        else:
            print('Intenta un número mas grande')

    print('Te quedan 2 intentos')
    num = int(input('Intenta otra vez: '))

    if num == adivina:
        print("ganaste!")
    else:
        if num > adivina:
            print('Intenta un número más pequeño')
        else:
            print('Intenta un número mas grande')

    print('Te quedan 1 intento')
    num = int(input('Intenta por última vez: '))

    if num == adivina:
        print("ganaste!")
    else:
        print('perdiste')





# --------------------------------ADIVINA NUM 2.0 -------------------------------------
def adivina2():
    import random

    # variables para modificar el juego

    intentos = 0
    limite = 20

    adivina = random.randint(1, limite)
    nombre = input(f'Hola, cómo te llamas?: ')
    print(
        f'Hola {nombre}, vamos a ver si puedes adivinar el número que estoy pensando entre 1 y 20, solo tienes 5 intentos')

    while intentos <= 4:
        numero = int(input('Intenta adivinar un número entre 0 y 20: '))
        if intentos < 4:
            if numero == adivina:
                print('GANASTE')
                break
            else:
                if numero > adivina:
                    print('intenta un número mas pequeño')
                else:
                    print('intenta un número mas grande')
            print(f'Te quedan {4 - intentos} intentos')
        else:
            if numero == adivina:
                print('GANASTE')
                break
            else:
                print('perdiste')
        intentos += 1




# --------------------------------ADIVINA NUM 3.0 -------------------------------------
# computador debe adivinar el numero que la persona piensa

def adivina3():
    import random

    minimo = 0
    maximo = 100
    intentos = 0

    cpu = random.randint(range(minimo, maximo))
    print(f'Piensa un número entre el 1 y 100 y yo intentaré adivinar cual és: '
          f'\nTu numero es {cpu}?')

    while intentos >= 0:

        jugador = input().lower()

        if jugador == 'si':
            print(f'adivine en {intentos + 1} intentos')
            break

        if jugador == 'no':
            opcion = input(f'1) intenta un número más grande'
                           f'\n2) intenta un número más pequeño\n ')

            if opcion == '1':
                cpu = random.randint(range(cpu, maximo))
                print(f'Tu numero es {cpu}?')

            if opcion == '2':
                cpu = random.randint(range(minimo, cpu))
                print(f'Tu numero es {cpu}?')
        intentos += 1






