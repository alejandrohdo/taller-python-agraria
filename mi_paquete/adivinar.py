import random
numero = random.randrange(1,10)
while True:
	valor = input("INGRESE EL NUMERO:")
	if numero == int(valor):
		print ("ADIVINASTE..!")
		break
	else:
		print("SIGUE INTENTANDO...!")