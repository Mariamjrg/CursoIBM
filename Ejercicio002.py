#Escribí un programa que solicite al usuario ingresar un número 
#con decimales y almacenalo en una variable. 
# A continuación, el programa debe solicitar al usuario que 
# ingrese un número entero y guardarlo en otra variable. 
# En una tercera variable se deberá guardar el resultado de la suma 
# de los dos números ingresados por el usuario. 
# Por último, se debe mostrar en pantalla el texto 
# “El resultado de la suma es [suma]”, donde “[suma]” 
# se reemplazará por el resultado de la operación.

n1=float(input('Ingresa número decimal:'))
n2=int(input('Ingresa número entero:'))
n3=n1+n2
print('el resultado de la suma es',n3)


