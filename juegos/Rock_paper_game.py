
# Juego piedra, papel, tijeras

def main():
    import random
    choice = input(f'{name} vamos a jugar piedra, papel o tijeras, ingresa tu elección: ').lower()
    list = ['piedra', 'papel', 'tijeras']
    cpu = random.choice(list)

    if cpu == choice:
        print('es un empate\n')

    elif choice == 'piedra':
        if cpu == 'papel':
            print(f'perdiste, {cpu} contra {choice}\n')
        elif cpu == 'tijeras':
            print(f'ganaste, {cpu} contra {choice} \n')

    elif choice == 'tijeras':
        if cpu == 'piedra':
            print(f'ganaste, {cpu} contra {choice} \n')
        elif cpu == 'papel':
            print(f'ganaste, {cpu} contra {choice} \n')

    elif choice == 'papel':
        if cpu == 'tijeras':
            print(f'ganaste, {cpu} contra {choice} \n')
        elif cpu == 'piedra':
            print(f'ganaste, {cpu} contra {choice} \n')

    else:
        print('Entrada inválida\n')


name = input('Hola, cómo te llamas?: \n ')
main()

while True:
    print('Ingresa (1) para volver a jugar o (2) para salir del juego')
    opcion = input('>')

    if opcion == '1':
        main()
    if opcion == '2':
        print('Gracias, has salido del juego')
        break








