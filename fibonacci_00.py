# Fibonacci-Sequence
# recursive

# Fibonacci-Sequence (0,1,1,2,3,5,8,13...)
# 0. --> 0
# 1. --> 1
# 2. --> 1 = 1+0
# 3. --> 2 = 1+1
# 4. --> 3 = 2+1
# ...
#
# n = 0,1,2,3,4,5...


# n. Fibonacci-Number
def fibonacci(n):
	if n == 0:
		fibo_n = 0
	elif n == 1:
		fibo_n = 1
	else:
		fibo_n = fibonacci(n-1)+fibonacci(n-2)
	return fibo_n

# Fibonacci-Sequence up to n-th Element 
def fibonacci_sequence(n):
	fibo_folge = []
	for i in range(n+1):
		fibo_folge.append(fibonacci(i))
	return fibo_folge

# Fibonacci with Input
def fibonacci_input():
	warning = "Invalid Input!"
	while True:
		try:
			n = int(input("Which Fibonacci-Number do you want to calculate? [0,1,2,3...]\nn: "))
			if n < 0:
				print(warning)
			else:
				break
		except:
			print(warning)

	while True:
		try:
			f = str(input("With Sequence? [y/n]\n"))	
			if f == "y" or f == "n":
				break
			else:
				print(warning) 
		except:
			print(warning)
			
	if f == "y":
		tmp = fibonacci_sequence(n)
		print(str(n)+". Fibonacci-Number: "+str(tmp[-1]))
		print("Fibonacci-Sequence up to "+str(n)+"-th Element: "+str(tmp)+"\n")
	elif f == "n":
		print(str(n)+". Fibonacci-Number: "+str(fibonacci(n))+"\n")

# Test
if __name__ == "__main__":
	n = 7
	print(str(n)+". Fibonacci-Number: "+str(fibonacci(n)))
	print("Fibonacci-Sequence up to "+str(n)+"-th Element: "+str(fibonacci_sequence(n))+"\n")
	fibonacci_input()
