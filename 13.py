a = int(input())
b = int(input())
c = int(input())

disc = (b**2) - (4*a*c)

if(disc > 0):
	print("İki adet çözüm bulundu ! ")
	x1 = (-b - (disc**0.5))/(2*a)
	x2 = (-b + (disc**0.5))/(2*a)
	print("Kökler : ",x1,x2)
elif(disc==0):
	print("Bir adet çözüm bulundu ! ")
	x1 = (-b - (disc**0.5))/(2*a)
	print("Kök : ",x1)
else:
	print("Kök bulunamadı")
