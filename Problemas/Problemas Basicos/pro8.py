pbank=10
bphone=120
cant = int(input("Escribe un numero"))*60

Total=cant/(pbank+bphone)



print("\n\n\n 8- Joel quiere que hacer varios viajes alrededor del mundo y sabe"
      "que en ciertos viajes no tendrá electricidad pero no quiere quedarse sin "
      "pila hasta llegar a su destino, así que decide comprar power banks para "
      "poder suplir de energía a su smartphone. La batería de su teléfono dura "
      "2 horas, al apagarse Joel puede conectar power bank y tiene que esperar "
      "10 minutos a que se cargue de nuevo su teléfono. ¿Cuántas power banks necesita"
      "comprar suponiendo que su viaje dura N cantidad de horas? \n")


print ("La cantidad power banks son" , round(Total,2))
