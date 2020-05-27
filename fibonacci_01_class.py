# Fibonacci-Sequence with class
# recursive

# Fibonacci-Sequence (0,1,1,2,3,5,8,13...)
# 0. --> 0
# 1. --> 1
# 2. --> 1 = 1+0
# 3. --> 2 = 1+1
# 4. --> 3 = 2+1
# ...
#
# n = 0,1,2,3,4,5... (not foolproof)

# constructor --> n = 5

# change n
# change_n(n)

# n. Fibonacci-Number
# fibonacci_n(n-optional)

# Fibonacci-Sequence up to n
# fibonacci_sequence(n-optional)

# Fibonacci-Path up to n
# fibonacci_path(n-optional)


class Fibonacci:
	def __init__(self, n=5):
		self.n = n

# change n
	def change_n(self, n):
		self.n = n

# n. Fibonacci-Number
	def fibonacci_n(self,n=""):
		if n == "":
			n = self.n
		if n == 0:
			fibo_n = 0
		elif n == 1:
			fibo_n = 1
		else:
			fibo_n = self.fibonacci_n(n-1) + self.fibonacci_n(n-2)
		return fibo_n

# Fibonacci-Sequence up ton
	def fibonacci_sequence(self,n=""):
		if n == "":
			n = self.n
		fibo_seq = []
		for i in range(n+1):
			fibo_seq.append(self.fibonacci_n(i))
		return fibo_seq

# Fibonacci-Path up to n
	def fibonacci_path(self,n=""):
		self.s = 0
		if n == "":
			n = self.n
		self.fibo_path = []									# empty Array
		self.fibo_path = self.fibonacci_n_path(n)			# Path-Array
		self.fibo_path = self.sort_path(self.fibo_path)		# sort Path-Array
		self.print_path(self.fibo_path)						# print Path

# Auxiliary Function
# Fibonacci-Path according to end of calculation
	def fibonacci_n_path(self,n,LR="",woher="",s=0):
		if LR == "":
			LR = "-"
		if woher == "":
			woher = n
		self.s += 1
		tmp = []
		tmp.append(self.s)	# Sequential Number of Start
		tmp.append(woher)	# Where was it started from?
		tmp.append(LR)		# Left/Right
		tmp.append(n)		# Which Element of Sequence
		if n == 0:
			fibo_n = 0
		elif n == 1:
			fibo_n = 1
		else:
			n_1 = self.fibonacci_n_path(n-1,"L",n,self.s)[-1][-1]
			n_2 = self.fibonacci_n_path(n-2,"R",n,self.s)[-1][-1]
			fibo_n = n_1 + n_2
		tmp.append(fibo_n)	# Wert
		self.fibo_path.append(tmp) 
		return self.fibo_path

# Auxiliary Function
# Path sortieren according to beginning of calculation
	def sort_path(self,x):
		L = len(x)
		for i in range(L-1):
			for j in range(i+1,L):
				if x[i][0] >= x[j][0]:
					tmp = x[i]
					x[i] = x[j]
					x[j] = tmp
		return x

# Auxiliary Function
# Print Path
	def print_path(self,x):
		L = len(x)
		s = ""
		for i in range(L):
			if i == 0:
				a = ""
			elif i == 1:
				a = " "
			else:
				if x[i][2] == "L" and x[i-1][2] == "L":		# Left, Left --> |
					s = s +"|"
				elif x[i][2] == "R" and x[i-1][2] == "L":	# Left, Right --> nothing 
					s = s
				elif x[i][2] == "R" and x[i-1][2] == "R":	# Right, Right --> ...
					s = list(s)
					rr = 1									#	once you have to delete in any case (*)
					for j in range(-1,-len(s),-1):			# 	--> rr: how many " " are there at the end of the previous row in a row
						if s[j] == " ":
							rr += 1
						else:
							break
					s = list(s)
					if s[-1] == " ":						# rr-times delete the last Elements of previous row
						for k in range(rr):
							del(s[-1])
					else:									# delete just the last Element of previous row (*)
						del(s[-1])
					s = "".join(s)
				elif x[i][2] == "L" and x[i-1][2] == "R":	# Right, Left --> " ", because the previous pair closed
					s = s + " "
			print(a+s+str(x[i][-1]))

# Test
if __name__ == "__main__":
	f = Fibonacci()
	print("n: "+str(f.n))
	print()

	f.change_n(7)
	print("n: "+str(f.n))
	print()

	n = 2
	print(str(n)+". Fibonacci-Number: "+str(f.fibonacci_n(n)))
	print()

	n = 3
	print("Fibonacci-Sequence up to "+str(n)+": "+str(f.fibonacci_sequence(n)))
	print()

	print("Fibonacci-Sequence up to "+str(f.n)+": "+str(f.fibonacci_sequence()))
	print()

	n = 5
	print("Fibonacci-Path up to "+str(n)+":")
	f.fibonacci_path(n)
	print("Steps: "+str(f.fibo_path[-1][0]))
	print()

	print("n: "+str(f.n))
