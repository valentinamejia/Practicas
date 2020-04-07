# CALCULADORA BÁSICA - PROYECTO NRO 1
# Socilicitar al usuario 2 números y realizar la suma de ellos

# Declaramos las variables
# Utilizamos input para que se guarde lo que el ususario ingresa
num1 = input('Ingresa un número: ')
num2 = input ('Ingresa otro número: ')

# Realizamos la suma y guardamos su resultado
# el input guarda como string, debemos convertir num en números

sum = float(num1) + float(num2)
res = float(num1) - float(num2)
mul = float(num1) * float(num2)
div = float(num1) / float(num2)

# Imprimimos el resultado y un mensaje de despedida
print('suma:', int(sum), '\n''resta:', int(res), '\n' 'multiplicación:',int(mul), '\n' 'división:', int(div))
print('Gracias')


