f = open("users.txt","r")

d = {}

for i in f:
	a = i.split(",")
	isim = a[0]
	sifre = a[1]
	sifre = sifre.replace("\n","")
	d[isim] = sifre

loginAd = input("İsminizi girin : ")
count=0
while(count<3):
	loginSifre = input("Şifrenizi girin : ")
	if((loginAd in d.keys()) and (d[loginAd] == loginSifre)):
		print("Giriş Başarılı !")
		break
	else:
		print("Giriş başarısız !")
	count+=1
