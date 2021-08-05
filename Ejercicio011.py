#Ejercicio10
#Escribí un programa que le solicite al usuario ingresar una fecha 
#formada por 8 números, donde los primeros dos representan el día, 
# los siguientes dos el mes y los últimos cuatro el año (DDMMAAAA).
# # Este dato debe guardarse en una variable con tipo int (número entero). 

fecha=int(input('Fecha en formato DDMMAAAA:'))
# Finalmente, mostrar al usuario la fecha con el formato DD / MM / AAAA.

DD=fecha//1000000
resto1=fecha%1000000
mes=resto1//10000
MM=str(mes)
AA=resto1%10000
print(DD,'/',MM,'/',AA)

#Solución propuesta
año=fecha%10000
dia=fecha//1000000
mes=(fecha//10000)%100
print(dia,"/",mes,"/",año)