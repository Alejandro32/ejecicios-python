
print("\n\n\n 1- Arnoldo le gustan mucho los números y quiere saber más de ellos,"
	  "él denomina números cool a los que son divisibles entre 3 y 5, el quiere crear"
	  "un programa en el cual el ingrese un número y le diga si es cool o no, ¿puedes ayudarlo? \n")

numero = int(input("\n Escribe un numero___"))


if numero % 5 ==0 and numero % 3 == 0:
	
	print("Es cool")

else:
	print("No esta cool")


