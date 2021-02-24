if(False):
	print("Birinci durum")
elif(True):
	print("İkinci durum")

a = int(input("Birinci sayıyı giriniz : "))
b = int(input("İkinci sayıyı giriniz  : "))
c = int(input("1.Toplama 2. Çıkarma 3.Çarpma 4.Bölme : "))

def topla(x,y):
	return(x+y)
def cikar(x,y):
	return(x-y)
def carpma(x,y):
	return(x*y)
def bolme(x,y):
	return(x/y)

if(c==1):
	print(topla(a,b))
elif(c==2):
	print(cikar(a,b))
elif(c==3):
	print(carpma(a,b))
elif(c==4):
	print(bolme(a,b))
