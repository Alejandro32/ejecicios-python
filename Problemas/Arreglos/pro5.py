
import random
certi=[]
tiempo=0

print("\n\n\n 5. Joel se da cuenta que no es el único con ese problema y quiere hacer "
	  " un algoritmo similar al anterior para que lo puedan utilizar más personas,  "
	  " ¿Que necesitaría cambiar?\n")

numero=int(input("Ingresa El numero delibros___"))
nombre=input("Ingresa El nombre de Alumno___")
certi=range(0,numero)
print("\n\n\n\n\n\n\n\n\nLa consulta para el Alumno",nombre,"\n")

for i in range(0,numero):

	paginas=random.randint(10,100)
	tiempo=paginas*2
	print("Por el libro",certi[i],"que contiene",paginas,"paginas","el tiempo que le tiene que invertir es",tiempo,"minutos")
  