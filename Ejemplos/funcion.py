def es_par(numero):
	return numero % 2 == 0

numero = int(input("Escribe un numero"))

if es_par(numero):
	print("Es par")
else:
    print("No es par")	

