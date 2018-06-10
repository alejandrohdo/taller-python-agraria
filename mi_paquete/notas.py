n1 = float(input("INGRESE NOTA1 :"))
n2 = float(input("INGRESE NOTA2 :"))
n3 = float(input("INGRESE NOTA3 :"))
promedio = (n1 + n2 + n3)/3
# if promedio >= 10.5 and promedio<= 20:
# 	print("APROBADO")
# else:
# 	if promedio >=8 and promedio <10.5:
# 		print("DESAPROBADO")
# 	else:
# 		print ("REPROBADO..!")
if promedio >= 10.5 and promedio<= 20:
	print("APROBADO")
elif promedio >=8 and promedio <10.5:
	print("DESAPROBADO")
elif promedio <8 and promedio >0:
	print ("REPROBADO..!")
else:
	print ("OPCION NO VALIDA ...")
