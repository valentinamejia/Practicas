#----------------------CONJUNTOS Y DICCIONOARIOS----------------------------------------

# [] listas  organizados y mutables
#  () tuplas  organizados e inmutables
#  {} conjuntos y diccionarios no estan organizados y solo cuenta un dato, no importa si esta repetido

dias = {
    'lun': 'lunes',
    'mar': 'martes',
    'mie': 'miercoles',
    'jue': 'jueves',
    'sab': 'sabado',
    'dom': 'domingo'

}

# no viene ordenado por tanto no funciona decir dias[1] no hay posición
#devuelve el dato del diccionario, sino existe nos devuelve un valor por defecto, no aparece error
print(dias.get('lun'))
print(dias.get('el identificador no existe'))

#pop elimina lunes del diccionario
print(dias.pop('lun'))

# popitem elimina el ultimo valor, noss devuelve la llave y el valor que elimina
print(dias.popitem())

# update cambia o modifica los datos, si no existe el dato entonces agrega el valor al diccionario
dias.update(lun='otro dia')
print(dias)

dias.update(vier = 'viernes\n')
print(dias)

#---------------------------BUCLES WHILE-----------------------------------------
i = 1

while i <= 5:
    print(i)
    i += 1 # es lo mismo a i = i + 1

print('termino el bucle\n')

#ahora i vale 6 ya que su última accion fue i +=1
print(i, '\n')

#---------------------------BUCLES FOR-----------------------------------------
dias = ['lunes', 'martes','miercoles','jueves']

for letra in 'Academia':
    print(letra, '\n')

for l in dias:
    print(l)

dias = {
    'lun': 'lunes',
    'mar': 'martes',
    'mie': 'miercoles',
    'jue': 'jueves',
    'sab': 'sabado',
    'dom': 'domingo'

}
dias = dias.items()
print(dias)
#items nos devuelve la clave y el valor del diccionario

dias = {
    'lun': 'lunes',
    'mar': 'martes',
    'mie': 'miercoles',
    'jue': 'jueves',
    'sab': 'sabado',
    'dom': 'domingo'

}

for clave, valor in dias.items():
    print(clave, '\n')
    print(valor, '\n' )

range(5) # devuelve 5 items 0,1,2,3,4 comenzando desde el cero

for indice in range (2,5): # del 2 al 5, serian 2,3,4 si coloco range(1,11,2) salta de dos en dos
    for indice2 in range(3)
    print(indice, indice2) # hace el primero y llega al segundo que lo hace 3 veces y vuelve al primer for

for indice in range(10):
    if indice == 4:
        print('Ganaste')
    else:
        print('no eres ganador')



#----------------------------BREAK AND CONTINUE -----------------------------------------------
# break rompe el for.
for indice in range(10):
    if indice == 4:
        break
        #si el print lo pongo despues del break, va a romper el programa y no muestra el 4,
        #si el print lo colocamos antes del break entonces aparece el 4 y posteriormente se cierra el programa o bucle
    print(indice)

# se salta el 4,
for indice in range(10):
    if indice == 4:
        continue
        #si el print lo pongo despues del continue, se salta el 4 y sigue con el bucle,
        #si el print lo colocamos antes del continue entonces aparece el 4 y no hace nada
    print(indice)

# --------------------------------LISTAS ANIDADAS --------------------------------------

grilla_numeros = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
#imprime las filas en orden
for filas in grilla_numeros:
    print(filas)

#imprime todos los datos en orden
for filas in grilla_numeros:
    for col in filas:
        print(col)

# --------------------------------ERRORES --------------------------------------

#try debe de estar acompañado de except
#se ejecuta hasta que exista un error, si hay error deja de ejecutar y va a los except
try:
    num1 = int(input('ingresa un número: '))
    num2 = 2
    print(num1)
    print(num1/num2)
# determino las excepciones o errores que el usuario comete
except ZeroDivisionError:
    print('no puedes dividir entre 0')
except ValueError:
    print('entrada invalida')
# else se ejecuta si no hubo ningun error
else:
    print('No hubo error')
# finally siempre se ejecuta
finally:
print('se ejecuta siempre')


#nos dice el mensaje de python del error cometido, la descripcion de Zerodivision o el que tengamos
except ZeroDivisionError as err:
    print(err)