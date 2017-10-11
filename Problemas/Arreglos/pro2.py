import random
Empleado=[]

print("\n\n\n 2. Antonio es el encargado de hacer la rifa de la compañía, cada empleado participa usando su clave de empleado y necesita determinar a un ganador. "
	  " ¿Puedes hacer un programa que le ayude a elegir al ganador de la rifa?\n")

numero=int(input("Ingresa numero de empleados___"))
Empleado=range(0,numero)
rifa=random.randint(0,numero)
#print(len(Empleado))
 
print("el ganador es",rifa)