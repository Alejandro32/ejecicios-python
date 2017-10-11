
import os


print("\n\n\n 4. Escribe un programa que calcule"
      " el factorial de una entrada N\n")

numero=int(input("Ingresa El numero___"))

fac=numero
for i in range(1,numero):
    fac=fac * i
  #os.system('clear')

print("El Factorial de",numero,"es____",fac) 
