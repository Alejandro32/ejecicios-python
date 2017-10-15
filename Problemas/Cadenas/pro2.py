pro=0


passw=input("Ingrese su password______")
num=len(passw)


for i in range(0,len(passw)):
 
 if passw[i]=="a" or  passw[i]=="A":
  passw=passw.replace("a"," ")
  passw=passw.replace("A"," ")
 

 elif passw[i]=="e" or passw[i]=="E":
  passw=passw.replace("e"," ")
  passw=passw.replace("E"," ")
 

 elif passw[i]=="i" or passw[i]=="I":
  passw=passw.replace("I"," ")
  passw=passw.replace("i"," ")

 elif passw[i]=="o" or passw[i]=="O":
  passw=passw.replace("O"," ")
  passw=passw.replace("o"," ")

 elif passw[i]=="u" or passw[i]=="U":
  passw=passw.replace("U"," ")
  passw=passw.replace("u"," ")




print("\n\n\n 2. Diego esta haUciendo un programa similar al de Anuar,"
	  " solamente que él no quiere sustituir vocales, el quiere desaparecerlas,"
	  " ¿puedes ayudarle?\n","La contaseña modificada es  ",passw)