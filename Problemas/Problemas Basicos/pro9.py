Gdl=25000
Cdmx=30000
Mty=40000
pconsulta=350
tconsulta=20
Jlaboral=8*30*tconsulta
TConsultorio=(Gdl+Cdmx+Mty)*2/pconsulta
cipdia=TConsultorio/(30*8)



print("\n\n\n 9- Daniel es un doctor que va a poner varios consultorios en México, Guadalajara y Monterrey."
	  "La renta en México es de $30000, en Guadalajara $25000 y en Monterrey $40000, Si cada consulta dura "
	  "20 minutos y el precio por consulta es de $350, ¿Cuantas consultas necesita hacer por consultorio hacer"
	  "al mes para duplicar la inversión (suponiendo cada mes tiene 30 días)? ¿Es posible que alcance la meta "
	  "suponiendo que su jornada laboral es de 8 horas? \n")


print ("La cantidad de consulta requeridas por mes son" , round(TConsultorio,0),"para duplicar la inversion")
print ("Citas por dia necesarias para duplicar la inversion" , round(cipdia,2))

