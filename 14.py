import random

rnd = random.randint(1,100) # 75

liste = []
print(rnd)
check = False
count = 0
while(count<5):
	n = int(input()) # 45,55,45
	if(n in liste):
		print("Daha önce girildi ! "),
	else:
		if(rnd==n):
			check=True
			break
		elif(n<rnd):
			print("Sayını arttır ! ")
		elif(n>rnd):
			print("Sayını küçült ! ")
	count+=1
	liste.append(n)
if(check==True):
	print("Oyunu kazandın ! ")
else:
	print("Oyunu kaybettin ! Sayı : ",rnd)
