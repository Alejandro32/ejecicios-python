import random
kyogre=100
pikachu=0
fight=100
print("\n\n\n 8. Joel es un maestro pokemon que va viajando por chapalita, "
	  " en su camino se encuentra a kyogre un pokemon legendario, kyogre es "
	  " un pokemon tipo agua y Joel tiene a un pikachu que es de tipo eléctrico, "
	  " en el primer ataque uso un ataque para paralizar a kyogre así que no puede "
	  " atacar. Kyogre tiene 100 puntos de vida, en cada ataque de pikachu logra hacer "
	  " un daño entre 2 a 5 puntos, para lograr capturarlo kyogre debe tener menos de 5 "
	  " puntos y más de 0. ¿Podrías hacer un algoritmo que haga una simulación de la "
	  " batalla y nos ayude a capturarlo? \n")

for i in range(1,51):
 pikachu=random.randint(2, 5)
 fight=kyogre-pikachu
 kyogre=fight

 if kyogre < 5 and kyogre > 0:
    kyogre=100
    pikachu=0
    fight=100
    break 

print("'Pokemon abatido'.","Necesitaste de ",i,"ataques listo para ser capturado")