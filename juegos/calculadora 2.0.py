
# SELECCIÓN DE CALCULADORA BÁSICA NRO 2
# Permite la opición de una de cuatro de las opeeraciónes básicas

# Declaramos las variables

num1 = float(input('Ingresa un número: ' ))
num2 = float(input('Ingresa otro número: ' ))

# Damos opciones de las operaciones
choice = input("selecciona la operación deseada: \n1.Suma \n2.Resta \n3.Multiplicación \n4.División \n")

# Ejecutamos las operaciones según la opción escojida
if choice == '1':
    sum = num1 + num2
    print(sum)

elif choice == '2':
    res = num1 - num2
    print(res)

elif choice == '3':
    mul = num1 * num2
    print(mul)

elif choice == '4':
    div = num1 / num2
    print(div)

else:
    print('Respuesta inválida')

