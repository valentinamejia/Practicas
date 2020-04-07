# --------------------------- FUNCIONES --------------------------

# declara la funcion, despues de def va el nombre de la función
# debe de estar identado despues de :, es decir 4 espacios

# ----------------PROGRAMA: devuelve las dos primeras y dos últimas letras de una palabra--------------


def mix(pal):
    if len(pal) > 4:
        mix1 = pal [0:2] + pal [-2:]
        print(mix1)

    if len(pal) <= 4:
        print('invalid input')

mix(input('Ingrese una palabra: '))


# ------------------------PROGRAMA:  devuelve el año nacimiento y cumpleaños # 100---------------------

def age_hundred():
    name = input('Escribe tu nombre: ')
    age = int(input('escribe tu edad: '))
    year = 2019 + (100 - age)
    birth = 2019 - age

    print('\n'f'Hola {name}, naciste en {birth}, tu cumpleaños 100 sera en el año {year}')

age_hundred()



#--------------PROGRAMA: devuelve los números pares y dice cuantos hay en una lista----------------------


#lista de números
nums = input('Ingresa los números separados por comas:')


#convetir el input en una lista
lista = list(int(n) for n in nums.split(','))

#iniciar el conteo
count, count2 = 0, 0

#describir las condiciones de pares e impares
for n in lista:
    if n %2 == 0:
        count += 1
        print(n)
    else:
        count += 1
        print(n)

print(f'Tenemos {count} números pares y {count2} números impares')

#------------------- SEGUNDA OPCION DE CODIGO----------------

nums = input('Ingresa los números separados por comas:')
lista = list(int(n) for n in nums.split(','))

impar =[]
par = []

for i in lista:
    if i %2 == 0:
        par.append(i)
    else:
        impar.append(i)

print ('la lista de numeros pares es: ', par)
print ('La lista de numeros impares es: ', impar)

#-------------------- FUNCION : mayor entre tres números------------------------

def mayor_num(num1,num2,num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    if num2 >= num3 and num2>=num3 :
        return num2
    else:
        return num3

print(mayor_num(100,34,5))

#-------------------- FUNCION : reemplazar vocales para una determinada frase------------------------


def encriptar(frase,caracter):
    encriptada ='' # variable vacia que crea la frase dada, recordar que un string no es modificable

    # se mete a frase y si es consonante se va a else y me guarda la letra en encriptada, si es vocal se va a if y me escribe
    #lo que llevo en encriptada y me anexa una x.

    for letra in frase:
        if letra.lower() in 'aeiouáéíúó':
            if letra.isupper():
                encriptada = encriptada + caracter.upper()
            else:
                encriptada = encriptada + caracter
        else:
            encriptada = encriptada + letra
    return encriptada


while True:
    texto = input('Ingresa una frase:\n')
    caracter_elegido = input('Elige el carácter que deseas:\n')
    print(encriptar(texto, caracter_elegido))
    opcion = input('''\n Ingresa (1) para encriptar otra frase o (2) para salir del programa: 
    >''')
    if opcion == '2':
        break
    if opcion =='1':
        print('---------o--------\n')

# no es necesario agregar el == 1 ya que como es un ciclo infinito, se tiene que si es distinto de 2 se vuelve a
# repetir, es la unica condicion que si es 2 entonces se cierre

#------------------- FRASE AL REVES -------------------------

def reverse():
  user=input('type anything here')
  b = user.split()
  c = b[::-1]  #se usa [inicio fin y salto] si el salto es engativo se recorre hacia atras, : significa que es desde inicio a fin 
  d = " ".join(c)
  print(d)

#------------------- DUPLICADOS -------------------------

# Write a function that takes a list and returns a new list that contains
# all the elements of the first list minus duplicates.
def lista_duplicate():
    lista = input('ingresa una lista de cosas:').split()
    print(lista)
    y = []
    for letra in lista:
        if letra not in y:
            y.append(letra)
    print(y)

#------------------- PASSWORD LENGHT GENERATOR -------------------------
# generate a password with length "passlen" with no duplicate characters in the password

import string
import random
def pw_gen(size = 8, chars=string.ascii_letters + string.digits + string.punctuation):

	return ''.join(random.choice(chars) for _ in range(size))

#print(pw_gen(int(input('How many characters in your password?'))))

def pwd():
    pwd = ""
    count = 0
    length = int(input("How many characters would you like in your password? "))

    while count != length:                                # significa != no igual, mientras count sea distinto a length
        upper = [random.choice(string.ascii_uppercase)]
        lower = [random.choice(string.ascii_lowercase)]
        num = [random.choice(string.digits)]
        symbol = [random.choice(string.punctuation)]
        everything = upper + lower + num + symbol
        pwd += random.choice(everything)
        count += 1
        continue
    if count == length:
        print(pwd)

#------------------- PASSWORD LENGHT GENERATOR -------------------------
# tells if a number is prime and returns the divisor list

def prime_number():

    # range function only works with integers, we import the module numpy to work with floats range
    # the function arange (start, stop, step)
    import numpy
    # para simplicidad trabajaremos con enteros

    number = int(input('enter your number: '))
    listRange = list(range(1, number + 1))

    divisorList = []
    for numb in listRange:
        if number % numb == 0:
            divisorList.append(numb)

    if len(divisorList) == 2:
        print(f'{number} is prime, only has {divisorList} as divisors')
    else:
        print(f'{number} is not a prime number and the divisors are {divisorList}')

prime_number()

# ---------------------- BUSQUEDA BINARIA----------------------------------------------

lista = [0, 88, 72, 21, 14, 16, 90, 35, 47, 6, 68, 12, 10, 54, 41]
lista.sort() # organiza la lista de menor a mayor

# buscar el punto medioo
# comprobar que el punto medio es el numero buscado
# numero menor, disminuimos el final
# numero menor aumentamos  el inicio


def busqueda_binaria(valor):
    inicio = 0
    final = len(lista)- 1 # el ultimo indice, acordarse que la lista comienza en 0

    while inicio<=final:
        puntero = (inicio + final)//2 # // parte entera de la division
        if valor ==lista[puntero]:
            return puntero
        elif valor > lista[puntero]:
            inicio = puntero + 1
        else:
            final = puntero - 1
    return None

def buscar_valor(valor):
    res_busqueda = busqueda_binaria(valor)
    if res_busqueda is None:
        return f'el valor {valor} no se encontro '
    else:
        return f'el numero {valor} se encuentra en la posicion {res_busqueda}'


while True:
    respuesta = int(input('escribe el numero que deseas buscar: '))
    print(buscar_valor(respuesta))
    opcion = input('''\n Ingresa (1) buscar otro numero o (2) para salir del programa: 
    >''')
    if opcion == '2':
        break
    if opcion =='1':
        print('---------o--------\n')

#------------------------------- TIC TAC TOE SQUARE ------------------------
def print_lines(a):
    print(" ---" * a)
    print("|   " * (a + 1))
def print_lines2(a):
    print(" ---" * a)
def draw_board(x):
    y=x
    while(y):
        if x>=1:
            print_lines(y)
            x-=1
        elif x==0:
            print_lines2(y)
            break

print("hello user!!!! welcome ")
x=int(input("Enter the size of board u want to draw---> "))
draw_board(x)




