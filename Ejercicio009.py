#Ejercicio9
#Escribí un programa que solicite al usuario el ingreso de un texto 
# y almacene ese texto en una variable. 
texto=input('texto:')
# 
# A continuación, mostrar en pantalla la primera letra del texto 
# ingresado. 
print(texto[0])
# 
# Luego, solicitar que ingrese un número positivo menor a la cantidad 
# de # caracteres que tiene el texto que ingresó (por ejemplo, si escribió 
# la palabra “HOLA”, tendrá que ser un número entre 0 y 4) y 
# almacenar este número en una variable llamada indice.

print(len(texto))
indice=int(input('introduce un número entre 0 y:'))

# Mostrar en pantalla el carácter del texto ubicado en la posición 
# dada por indice.
print(texto[indice])


