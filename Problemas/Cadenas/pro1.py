
num=0



passw=input("Ingrese su password______")
num=len(passw)


for i in range(0,len(passw)):
 
 if passw[i]=="a" or  passw[i]=="A":
  passw=passw.replace("a","4")
  passw=passw.replace("A","4")
 

 elif passw[i]=="e" or passw[i]=="E":
  passw=passw.replace("e","3")
  passw=passw.replace("E","3")
 

 elif passw[i]=="i" or passw[i]=="I":
  passw=passw.replace("I","1")
  passw=passw.replace("i","1")

 elif passw[i]=="o" or passw[i]=="O":
  passw=passw.replace("O","0")
  passw=passw.replace("o","0")



print("\n\n\n 1. Anuar quiere hacer sus contraseñas más seguras, se da cuenta que puede cambiar vocales por números"
      " a = 4, e = 3, i = 1, o = 0. ¿Podrías hacer un programa que reciba una contraseña, la altere sustituyendo las "
      " vocales y al final la imprima?\n","La contaseña modificada es  ",passw)