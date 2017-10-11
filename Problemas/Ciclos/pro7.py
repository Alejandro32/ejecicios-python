

import random
lanza=0
lanza1=0
cont=0
cont1=0
print("\n\n\n 7. Basado en su estudio anterior Anuar quiere hacer un estudio similar, "
	  " pero ahora usando 2 dados, ¿podrías ayudarlo a modificar su algoritmo para lograr "
	  " su objetivo?.\n")

numero=int(input("Ingresa el numero de lanzamientos__"))

for i in range(1,numero +1):
 dado=random.randint(1, 6)
 dado1=random.randint(1, 6)
 lanza= dado % 2
 lanza1= dado1 % 2

 if lanza == 0:
  cont =cont + 1 
  print("Lanzamiento_",i,"Dado 1 resultado de lanzamiento__",dado)
  dado=0
 if lanza1 == 0:
  cont1 =cont1 + 1 
  print("Lanzamiento_",i,"Dado 2 resultado de lanzamiento__",dado1)
  dado1=0
print("\nEl total de numeros de lanzamientos par es ","Dado1=",cont,"Dado2=",cont)