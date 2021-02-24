kullaniciList = ["batuhan@ayhan.com","ahmet@mehmet.com","fatih@purtas.com"]
sifreList     = ["123","456","145"]

kullaniciDict = {"batuhan@ayhan.com":"123","ahmet@mehmet.com":"456","fatih@purtas.com":"145"}

c = 0
while(c!=1):
	email = input("Kaydolmak için email'inizi girin : ")
	sifre = input("Kaydolmak için sifre girin : ")

	if(("@" and "." in email) and (email not in kullaniciList)):
		kullaniciList.append(email)
		sifreList.append(sifre)
		kullaniciDict[email] = sifre
		print("Kayıt tamamlandı")

	elif(email in kullaniciList):
		print("Kullanıcı zaten kayıtlı")
	else:
		print("Kayıt tamamlanamadı")

	c = int(input("Login için 1 yazın ! : "))

d = input("Email : ")
e = input("Şifre : ")

if(d in kullaniciList):
  if(kullaniciDict[d]==e):
    print("Giriş tamamlandı :)")
  else:
    print("Hatalı giriş yaptınız!!!")
else:
	print("Email kayıtlı değil ! ")
