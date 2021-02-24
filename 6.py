def boolFunction(string):
    if "@" and "." in string:
        return True
    else:
        return False

print(boolFunction("batuhanayhan@cs.hacettepe.edu.tr"))

#####################################################
# 1
# 1 2
# 1 2 3
# 1 2 3 4
a = int(input())
for i in range(1, a+1):
    for j in range(1, i + 1):
        print(j, end=' ')
    print("")

############################
def isFirst_And_Last_Same(numberList):
    print("Given list is ", numberList)
    firstElement = numberList[0]
    lastElement = numberList[-1]
    if (firstElement == lastElement):
        return True
    else:
        return False
numList = [10, 20, 30, 40, 10]
print("result is", isFirst_And_Last_Same(numList))

#################
string = "125"
new = ""
for i in string:
	new = i + new
print(new)
