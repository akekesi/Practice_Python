# Fibonacci-Sequence with list (Zwischenspeicher)
# recursive with list

# Fibonacci-Sequence (0,1,1,2,3,5,8,13...)
# 0. --> 0
# 1. --> 1
# 2. --> 1 = 1+0
# 3. --> 2 = 1+1
# 4. --> 3 = 2+1
# ...
#
# n = 0,1,2,3,4,5...


import time

fibo_list = [0]
s = 0

def fibonacci_list(n):
	global s
	s += 1
	try:
		fibo_n = fibo_list[n]
	except:
		if n == 0:
			fibo_n = 0
		elif n == 1:
			fibo_n = 1
		else:
			fibo_n = fibonacci_list(n-1) + fibonacci_list(n-2)
		fibo_list.append(fibo_n)
	return fibo_n

#Test
if __name__ == "__main__":
	n = 13
	print(str(n)+". Finoacci-Number: "+str(fibonacci_list(n)))
	print("Fibonacci-Sequence: "+str(fibo_list))
	print("Steps: "+str(s))
	s = 0
	print()
	
	n = 222
	time_start = time.time()
	print(str(n)+". Finoacci-Number: "+str(fibonacci_list(n)))
	time_end = time.time()
	print("Steps: "+str(s))
	print("Time: "+str(time_end-time_start))
	s = 0

