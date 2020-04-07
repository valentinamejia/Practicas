# Obtener la fecha y hora actuales

import datetime

ahora = datetime.datetime.now()

print(ahora)
print(ahora.strftime('%d/%m/%Y %H:%M%S' "\n") )

print(datetime.date.today().year)

#strftime cadena de formateo

#

hora = ahora.time()
fecha = ahora.date()

print(hora, "\n")

print(fecha)


print(hora.hour, hora.minute, hora.second)  # propiedades del objeto Hora
print(fecha.year, fecha.month, fecha.day, 'stop' )  # propiedades del objeto Fecha

import time

print(time.strftime("%H:%M:%S"))   #formato del tiempo hora 24 minuto y segudo
print(time.strftime("%I:%M:%S"))   #formato del tiempo hora 12 minuto y segudo

print(time.strftime("%d/%m/%y"))


# %c Fecha y tiempo

formato = "%c"
ahora =time.strftime(formato)
print ('\n',ahora, "\n" )


# %x fecha
# %x tiempo

format ="%x"
now = time.strftime(format)
print(now,'\n')


fecha = "21/01/1991"
fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y" )
print(fecha)
# p parse, una transformacion de tu cadena de texto a tipo fecha


fecha_mod  = fecha + datetime.timedelta(days= 3, weeks = 1,  hours = 1)
print(fecha_mod)

#corre la fecha actual segun las operacion dadas

# https://www.programiz.com/python-programming/datetime/current-datetime relacionado
# con date y tiempos actuales