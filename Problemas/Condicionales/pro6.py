


print("\n\n\n 6. Paco está haciendo un videojuego y necesita"
      " hacer un programa que determine la jerarquía de usuario"
      " de acuerdo a su nivel, las jerarquías son paladin : nivel"
      " 0 -10, caballero dorado : nivel 11 - 30, dios destructor: "
      " 31 - 50.\n")

numero = int(input("\n Escribe un numero___"))


if numero >= 0 and numero <= 10:

	print("Es de Jerarquia Paladin")

elif numero >= 11 and numero <= 30:
	print("Es de Jerarquia Caballero Dorado")

elif numero >= 31 and numero <= 50:
	print("Es de Jerarquia Dios Destructor")	

else:
	print("No es un rango valido")


