
print("Valor del dolar sugerido = 18.3   Valor del euro= 21.5228\n")

vdolar = int(input("\n  Escribe tasa de cambio del dolar___"))
vdeuro = int(input("\n  Escribe tasa de cambio del euro____"))

Mex=130000
Usa=1000*1.10*vdolar
Esp=990*1.09*vdeuro

print ("Mexicano  =",round(Mex,2))
print( "Americano =",round(Usa,2))
print ("Español   =",round(Esp,2))

#vres = varchar(input("Introduce la respuesta"))
print("\n\n\n10. Anuar quiere poner un negocio de videojuegos, para ello necesita comprar"
      "varios Nintendo Switch  como primera consola. El tiene 3 posibles proveedore "
      "americano, un mexicano y uno español todos. Anuar tiene $50000 pesos en el banco."
      "El proveedor americano le cobra $1000 dólares por unidad y el costo de aduanas "
      "es de 10% de su compra y envío gratuito, el proveedor mexicano le cobra $13000 pesos" 
      "por unidad y envío gratuito, El proveedor español $990 euros por unidad y el costo de"
      "aduanas es de 9% de su compra y envio gratuito, ¿Que proveedor le conviene elegir a Anuar? \n\n\n")


print ("La mejor compra sugerida es de:  ",Mex)