#kullanıcının girdiği 2 sayı arasındaki sayıların toplamını bulan program
a= int(input())
b= int(input())
sum = 0
for i in range(a,b):
    sum = sum + i
print(sum)

################################
#girilen sayının asal mı değil mi olduğunu bulan program
################################
sayi = int(input())

isPrime = True
for i in range(2,sayi):
    if  sayi % i == 0:
        isPrime = False
        break

if isPrime:
    print("Asaldır")
else:
    print("Asal değildir")


################################
# listede 5'e bölünebilen sayıları yazdır
def findDivisible(numberList):
    print("Given list is ", numberList)
    print("Divisible of 5 in a list")
    for num in numberList:
        if (num % 5 == 0):
            print(num)

numList = [10, 20, 33, 46, 55]
findDivisible(numList)
