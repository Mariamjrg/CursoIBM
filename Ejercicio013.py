#Ejercicio13
#Escribí un programa que le solicite al usuario su edad y la guarde 
#en una variable. Que luego solicite la cantidad de artículos comprados
#en una tienda y la guarde en otra variable. 

edad=int(input('Tu edad:'))
articulos=int(input('Artículos comprados:'))

# Finalmente, mostrar en pantalla un valor de verdad (True o False) 
# que indique si el usuario # es mayor de 18 años de edad y además
# compró más de 1 artículo.

print((edad>=18) and (articulos>1))
