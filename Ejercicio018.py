#Ejercicio18
#Escribe un programa que, solicite al usuario el ingreso de dos números
# diferentes y muestre en pantalla al mayor de los dos.

num1=float(input('Un número:'))
num2=float(input('Otro número distinto: '))

if num1>num2:
    print (num1, 'es mayor')
else:
    print (num2, 'es mayor')
