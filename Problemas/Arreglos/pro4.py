import random
certi=[]
tiempo=0
print("\n\n\n 4. Joel tiene que leer bastante para su exámen de certificación, en total "
	  "  tiene que leer N libros, cada uno con un número diferente de páginas, en promedio"
	  " Joel tarda 2 minutos por página, ¿Cuánto tiempo tardará Joel en leer cada libro?\n")

numero=int(input("Ingresa El numero delibros___"))
certi=range(0,numero)


for i in range(0,numero):

	paginas=random.randint(10,100)
	tiempo=paginas*2
	print("Por el libro",certi[i],"contiene",paginas,"paginas","tiempo invertido",tiempo,"minutos")
  