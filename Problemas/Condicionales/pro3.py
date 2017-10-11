

print("\n\n\n 3. Arnoldo sigue en su búsqueda de números,"
	  "ahora busca números raros. Los números raros son  "
	  "aquellos que son divisibles entre 5 y entre 3, pero"
	  " no entre 2. El quiere crear un programa en el cual "
	  " ingrese un número y le diga si es raro o no. \n")

numero = int(input("\n Escribe un numero___"))


if numero % 5 ==0 and numero % 3 == 0 and numero % 2 != 0:

	print("Es numero Raro ")

else  :
	print("No es numero raro")

