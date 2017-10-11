
import random
arti=[]

porce=0
print("\n\n\n 6. Orlando va a abrir una tienda de ropa, para llenarla va a comprar N "
	  " cantidad de artículos y cada articulo tiene cierto porcentaje de ganancia.   " 
	  " ¿Cuánto ganará Orlando por cada artículo?.\n")


numero=int(input("Ingresa El numero de articulos___"))
arti=range(0,numero)


for i in range(0,numero):

	porcentaje=random.randrange(20,100,20)
	print("El articulo",arti[i],"el porcentaje de ganancia es",porcentaje)
