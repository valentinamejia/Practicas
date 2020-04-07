# --------------------------------------------Strings--------------------------------------------

# Comillas dobles. Podemos poner dentro comillas simples sin problemas
cadena = "Hola ' Mundo"

print(cadena, "\n")

# Comilas simples. Podemos poner dentro comillas dobles sin problemas
cadena2 = 'Otro " Hola Mundo '

print(cadena2, "\n")

# Triples comillas. Podemos poner dentro lo que queramos (salvo comillas triples)
# sin problemas.


cadena3 = """En un lugar '
de la Mancha "
de cuyo nombre
no quiero acordarme"""

print(cadena3, "\n")

# \n nueva linea
# \t tabulador, como un espacio


cadena = "Hola Mundo"
for letra in cadena: print(letra)

# acceder directamente a los caracteres de la cadena usando []

# Hola Mundo
# 0123456789

cadena = "Hola Mundo"
letra = cadena[5]    #cuenta desde el cero

print (letra)
print(cadena[5])

letra = cadena [-5]    # hacia atras, comienza desde el -1

print (letra)
print(cadena[-5])

# desde la posicion 5 hasta antes del 9, no cuenta la novena letra
letras = cadena [5:9]

print (letras)

letras = cadena [5:]   # de la quinta hasta el final
letras = cadena [:9]   # desde el inicio hasta antes de la segunda


print (cadena.capitalize())  # str. es el nombre del string, del texto

# concatenar funciones, preguntar y cambiar las funciones

modificada = cadena.upper().isupper()
#vuelve la cadena en mayusculas y luego pregunta si esta capitalizada toda

print(modificada)

# str.split()  por espacios separa las palbras, str.split(' ') los separadores son
# los que se encuentran entre ' '.

cadena2 = "Wilson y willis se fueron a pasear"

print(cadena2.split())


cadena2 = "Wilson,willis,watson"

print(cadena2.split(','))
print(cadena2[3],"\n")

cadena = "Hola Mundo"

# Sacan True por pantalla.
print ( "o" in cadena, "\n" )
print ( "Hola" in cadena, "\n" )

# Sacan False por pantalla.
print ( "p" in "Hola Mundo", "\n" )
print ( "Pepe" in "Hola Mundo", "\n" )

cadena = "Hola Mundo"

# El método find de string nos permite buscar una subcadena dentro de la cadena.
# Este método admite hasta tres parámetros. La cadena a buscar, el índice a partir del cual
# empezar a buscar y el índice a partir del cual dejar de buscar. Nos devuelve la posición
# en donde ha encontrado la cadena, o -1 si no la encuentra.

print(cadena.find("Hola"))        # Devuelve posición 0
print(cadena.find("Mundo"))       # Devuelve posición 5

# Devuelve -1, a partir de la posición 3 de "Hola Mundo" no hay ningún "Hola"
print(cadena.find("Hola", 3))
# Devuelve 5, a partir de la posición 3 de "Hola Mundo" hay un "Mundo".
print(cadena.find("Mundo", 3))

# Devuelve 0, hay un "Hola" entre la posición 0 y 5 de "Hola Mundo".
print(cadena.find("Hola", 0, 5))

# Devuelve -1, no hay un "Mundo" entre la posición 0 y 5 de "Hola Mundo".
print(cadena.find("Mundo", 0, 5))

# find halla la primera posición
print (cadena.find("un"))    # El primer "un" está en la posición 0, devuelve 0

# rfind halla la última posición
print (cadena.rfind("un"))   # El último "un" está en la posición 16, devuelve 16


# .format para unir variables y cadenas

alumnos = 2500
academia = "Willis"

# alumnos se transforma en string, solo concatena letras, no números
cadena = "los" + str(alumnos) + " niños se parcen a" + academia
print(cadena)

# posición de las variables en la cadena por {}
cadena = "los {} niños se parecen a {}".format (alumnos, academia)
print(cadena)

#f de formato sin necesidad de format o de strin
cadena = f"los {alumnos} niños se parecen a {academia}"

# ---------------------------------LISTAS FUNCIONES--------------------------------------------

numeros = [5, 2, 23, 35, 10, 2]
frutas = [ 'Naranja', 'Manzana', 'Mango', 'Sandia']

# list
#len
# append  agregar a la lista
frutas.append('Banano')
print(frutas)

# cambiar el nombre de una posicion en la lista
frutas[1] = 'Cereza'
print(frutas)

# extend agregar una lista a otra
list2 = numeros + frutas
print(list2)

numeros.extend(frutas)
print(numeros) # modificamos la lista numeros y agregamos la lista frutas a esta

# insert() agrega dos parametros, el indice o posicion donde queremos se agrege el objeto, y segundo el objeto mismo
frutas.insert(2, 'Arandanos')

# remove, eliminar un objeto de la lista
frutas.remove('Banano')
# Elimina toda la lista
frutas.clear()
# pop elimina el último elemento de la fila
frutas.pop()
# index nos da el indice del objeto pedido
print(frutas.index('Banano'))
# count cuenta cuantas veces aparece un objeto en la lista
print(frutas.count('Kiwi'))
# sort organiza orden alfabetico y menor a mayor en numeros en la lista
numeros.sort()
numeros.reverse() # reversa los items de la lista
# copy copia exacta de otra lista, almacenada en otra variable
frutas = frutas.copy()

