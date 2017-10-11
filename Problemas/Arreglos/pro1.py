
promedio=[10,9,9,10,7,10,9]
cal=0

print("\n\n\n 1. Joel ya recibió sus calificaciones 10, 8, 9, 10, 7 , 10, 9. "
	  " ¿podrías sacar su promedio usando menos de 5 variables?\n")

for i in range(0,7):
  cal=promedio[i]+cal
print("El Promediode Joel es___",round(cal/7),2) 
