import random

t = ["Taş","Kağıt","Makas"]
index = random.randint(0,2)
computer = t[index]

while True:
	player = input("Taş, Kağıt, Makas = ")
	if player==computer:
		print("Berabere ! Bilgisayarın Cevabı : ",computer)
	elif player=="Taş":
		if(computer=="Kağıt"):
			print("Kaybettin ! Bilgisayarın Cevabı : ",computer)
		elif(computer=="Makas"):
			print("Kazandın ! Bilgisayarın Cevabı : ",computer)
	elif player=="Kağıt":
		if computer=="Taş":
			print("Kazandın ! Bilgisayarın Cevabı : ",computer)
		elif computer=="Makas":
			print("Kaybettin ! Bilgisayarın Cevabı : ",computer)
	elif player=="Makas":
		if computer=="Taş":
			print("Kaybettin ! Bilgisayarın Cevabı : ",computer)
		elif computer=="Kağıt":
			print("Kazandın ! Bilgisayarın Cevabı : ",computer)
	index = random.randint(0,2)
	computer = t[index]
