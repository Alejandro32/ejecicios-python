import os
pro=0

print("\n\n\n 3. Joel se da cuenta que su algoritmo quedo genial"
      " y quiere que más gente lo utilice, el problema es que "
      " algunos de sus compañeros no llevan las mismas materias "
      " que él, ¿podrías ayudarlo a modificar su algoritmo para "
      " solucionar ese inconveniente? \n")

mat=int(input("Ingresa El numero de Materias a promediar___"))
alum=input("Ingresa El Nombre del alumno a promediar___")
for i in range(0,mat):

   numero=int(input("Ingresa las calificaciones___"))
   pro=pro+numero
   os.system('clear')


print("El promedio de ",alum," es ________",round(pro/mat,2)) 
