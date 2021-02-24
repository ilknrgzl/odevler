def fibonacci(num): # 5
	i = 1
	if num == 1:
		fib = [0]
	elif num==2:
		fib = [0,1]
	elif num > 2:
		fib = [0,1,1]
		while(i<(num-1)):
			fib.append(fib[i]+fib[i+1])
			i+=1
	return fib

a = fibonacci(5)
print(a)
