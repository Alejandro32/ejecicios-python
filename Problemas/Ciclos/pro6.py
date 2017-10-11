
import random
lanza=0
cont=0
print("\n\n\n 6. Anuar está haciendo un estudio estadístico "
	  " sobre la probabilidad de que en N cantidad de lanzamientos "
	  " de un dado el número sea par, ¿Puedes ayudarlo?.\n")

numero=int(input("Ingresa el numero de lanzamientos__"))

for i in range(1,numero +1):
 dado=random.randint(1, 6)
 lanza= dado % 2
 if lanza == 0:
  cont =cont + 1 
  print("Lanzamiento_",i,"Numero de dado es__",dado)
  dado=0
print("\nEl total de numeros de lanzamientos par es ",cont)