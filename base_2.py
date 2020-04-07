
import math
suma = 0
cantidad = 0
L = []
M = []
for i in range(844,1845):
  if i % 5 == 0:
    ln = math.log(i)
    L.append(ln)
for i in range(2450,2844):
  if i % 3 == 2:
    t = i
    M.append(t)
for i in range(0,90):
  l = L[i]
  m = M[i]
  suma += (2*l) + m
  cantidad += 1
promedio = suma / cantidad
coseno = math.cos(promedio)
print (round(coseno,6))
print(cantidad)
print(suma)