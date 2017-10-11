inc=1
cont=0

print("\n\n\n 5. A Diego le encargaron de tarea investigar la"
      " cantidad de números divisibles entre 3 y 5 en una serie "
      " numérica que va de 1 a N, ¿Puedes apoyarlo?\n")

numero=int(input("Ingresa El rango del 1 al "))

for i in range(1,numero +1):
 entre3= i % 3
 entre5= i % 5
 if entre3 == 0 and entre5 == 0:
 	   cont =cont + 1 
 	   print("Numero encontrado en la serie es ",i)


print("\nEl total de numeros divisibles de la serie numerica ",cont)
