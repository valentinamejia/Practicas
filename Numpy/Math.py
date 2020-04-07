# LINK: https://repl.it/@manuelblaze/APyC-Fundamentos-de-Programacion-UNALMED

import math
from math import pi

def seno(a):
    # round(number, approximatted to six digits)
    sen = round(math.sin(a), 6)
    return sen


def cos(a):
    cos = round(math.cos(a), 6)
    return cos


def log_natural(a):
    ln = round(math.log(a), 6)
    return ln


def len_elementos(lista):
    return len(lista)


def absoluto(a):
    valor = abs(a)
    return valor


def promedio(lista):
    suma = 0
    for i in lista:
        suma += i
    prom = suma/len(lista)
    return prom


def suma(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

# function that sums a value to all elements in list
def suma_list(lista, n):
    sum_list = []
    for i in lista:
        sum_list.append(i+n)
    return sum_list


def raiz_cubica(lista):
    lista2=[]
    for i in lista:
        raiz=i**(1/3)
        lista2.append(raiz)
    return lista2

def exponencial(lista):
    lista2 = []
    for i in lista:
        exp = 2 ** i
        lista2.append(exp)
    return lista2


#----------------WISE ELEMENT OPERATIONS FUNCTION----------------------

def diferencia(lista1, lista2):
    list_diference =[]
    for x, y in zip(lista1, lista2):
        list_diference.append(x-y)
    return print(list_diference)


import numpy as np
list1 = [ int(i) for i in list(input('Input your first list: ').split(','))]
list2 = [ int(i) for i in list(input('Input your second list: ').split(','))]
x = np.array(list1)
y = np.array(list2)
print(x-y, '\n')

# en loop no se comienza en 0, sino en 1, entonces cuenta desde la posicion


def thrid_difference(lista1,lista2):
    list_diference = []
    for i in range(0,lista1):
        result = lista1[i] - lista2[i]
        list_diference.append((result))
    return list_diference

#----------------AREAS, PERIMETROS----------------------

def cir_perimeter(lista):
    lista2 = []
    for i in lista:
      perimeter = 2 * pi * i
      lista2.append(perimeter)
    return lista2

def cir_area(lista):
    lista2 = []
    for i in lista:
        area =  pi * (i**2)
        lista2.append(area)
    return lista2

def area_regular_area(n_sides, s_lenght):
    n_sides = int(input('Number of sides: '))
    s_lenght = float(input('Lenght of one side:'))
    area = (n_sides * (s_lenght ** 2)) / (4 * math.tan(pi / n_sides))
    print('the total area is: ', area)

import math

# calcular el seno de la suma de la raiz cubica de las areas de los cuadrados de lado 4L
# siendo L los numeros impares entre 4221 y 5368 a 6 cifras decimales

suma = 0
for i in range(4221,5369):
    if i % 2 !=0 :
        area_cubica = (4 * i) ** (2/3)
        suma += area_cubica

sen = round(math.sin(suma), 6)
print(' seno de la suma de raiz cubica de areas:', sen,'\n')

# calcular el coseno del promedio de los elementos de L, siendo L los numeros
# comprendidios entre 3186 y 4869

lista = []
for i in range(3187, 4870):
    if i % 2 == 0:
        suma += i
        lista.append(i)

promedio = suma / len(lista)
coseno = round(math.cos(promedio),6)
print('coseno del promedio de los elementos de L: ', coseno,'\n')

# coseno del promedio de los perimetros de los triangulos isoceles de lado
# L, L y M. L y M el logaritmo natural de los primerps 90 multiplos de 5
# entre 844 y 1844 y los primeros 90 numeros entre 2450 y 2844 cuyo modulo entre 3 sea igual
# a 2 respectivamente.


L = []
M = []
suma = 0
total = 0

for i in range(844, 1845):
    if i % 5 == 0:
        ln = math.log(i)
        L.append(ln)

for x in range(2450, 2845):
    if x % 3 == 2:
        M.append(x)

for i in range(0,90):
    per = 2*L[i] + M[i]
    suma += per
    total += 1

prom = suma / total
coseno = round(math.cos(prom), 6)
print('coseno del promedio de los perimetros de los triangulos:', coseno,'\n')

# logaritmo natural del valor absoluto de la suma de las diferencias entre las
# areas de un circulo de radio 2L y cuadrados de lado 3L. L son los pares entre
# 6811 y 10610 múltiplos de tres y cuatro simultaneamente.
suma = 0

for i in range(6811, 10611):
    if i % 2 == 0:
        if i % 3 == 0:
            if i % 4 == 0:
                area_circulo = math.pi * ((2*i)**2)
                area_cuadrado = (3 * i) ** 2
                diferencia = area_circulo - area_cuadrado
                suma += diferencia

suma1 =abs(suma)
ln1 = math.log(suma1)
print('logaritmo natural del valor absoluto de la suma:', ln1,'\n')

# coseno de la suma de los volúmenes de los cilindros de radio 3L/2 y altura 5M.
# Siendo L y M la raiz cubica de los primeros 20 numeros multiplos de 5 entre 1646 y 3646 y
# cuya division entera por 3 sea menor a 950 y multiplo de 5, y los 20 primeros numeros entre 1212 y 3646
# cuya division entera por 5 sea par.

radio = []
altura = []
suma = 0
for i in range (1646, 3647):
    if (i // 3) % 5 == 0 and (i // 3) > 950:
            radio.append(i)

for i in range (1212, 3647):
    if (i // 5) % 2 == 0:
        altura.append(i)

for i in range(0,20):
    vol =  3.14 * (((3 * radio[i])/2)**2)*(5 * altura[i])
    suma += vol

print('coseno de la suma de los volúmenes de los cilindros:', math.cos(suma), '\n')

# Calcule el seno del promedio de las áreas de los rectangulos de lados L y M.
# Siendo L y M los ultimos 45 numeros comprendidos entre 2958 y 4958 cuya
# division entera por 3 sea un numero par y el producto de 2 por el seno de los ultimos 45
# numeros impares comprendidos entre 6845 y 9958

L2 = []
M2 = []
suma2 = 0
for i in range(2958, 4959):
    if (i // 3) % 2 == 0:
        L2.append(i)
L2. reverse()

for i in range( 6845, 9959):
    if i % 2 != 0:
        M2. append(2 * math.sin(i))
M2.reverse()

for i in range(0,45):
 suma2 += L2[i] * M2[i]

 prom2 = suma2 / 45
print('seno del promedio de las áreas de los rectangulos: ', round(math.sin(prom2), 6), '\n')

# Calcule el coseno de la suma de las distancias entre los puntos (L/2 , 3M),(4L , 3M/2) para cada valor de L y M.
# Siendo L y M el logaritmo natural de los primeros 60 numeros multiplos de 5 comprendidos entre 7645 y 8729 y el
# producto de PI por el coseno de los primeros 60 numeros impares entre 1625 y 2435 respectivamente.
# (Tomar PI como 3,1416)

X1 = []
X2 = []
Y1 = []
Y2 = []
suma3 = 0
for i in range(7645, 8730):
    if i % 5 == 0:
        ln2 = math.log(i)
        X1.append(ln2/2)
        X2.append(4*ln2)

for i in range(1625, 2436):
    if i % 2 != 0:
        m = 3.1416 * math.cos(i)
        Y1.append(3*m)
        Y2.append((3/2) * m)

for i in range (0,60):
    dist = math.sqrt( (X1[i] - X2[i])**2 + (Y1[i] - Y2[i])**2)
    suma3 += dist

print('coseno de la suma de las distancias: ', round(math.cos(suma3), 6), '\n')




