# Matrix-Class

class Matrix:

# Konstruktor
	def __init__(self,*args):			# Eingabe: m, m, Werte als Liste
		self.w = "ERROR: INVALID INPUT!"
		if len(args) == 3:
			self.m = args[0]
			self.n = args[1]
			self.werte = args[2]
			self.check_nmw()
			self.matrix = self.erstellen_matrix(self.werte)
		else:							# Eingabe: Matrix 
			self.mat = args[0]
			self.check_mat()
			self.m = len(self.mat)
			self.n = len(self.mat[0])
			self.werte = self.get_werte(self.mat)
			self.matrix = self.erstellen_matrix(self.werte)

# Get values from matrix --> list
	def get_werte(self,matrix):
		werte = []
		for i in range(self.m):
			for j in range(self.n):
				werte.append(matrix[i][j])
		return werte

# Create matrix from list of values
	def erstellen_matrix(self,werte):
		num = 0
		matrix = [[0 for x in range(self.n)] for y in range(self.m)]
		for i in range(self.m):
			for j in range(self.n):
				matrix[i][j] = werte[num]
				num += 1
		return matrix

# Overload __str__
	def __str__(self):					# __str__ a kiiratas überladen, ha ki #-gelem,
		return str(self.matrix)			# akkor csak az Klasse nevet irja ki (lehet tesztelni, hogy Klasse-e, vagy csak siman matrix)

# Print matrix
	def print_matrix(self):
		print(self.matrix)

# Transpose matrix --> return just a matrix (not ojbect of class)
	def transp_csak(self):				# itt transzponalja a matrixot es visszaad egy matrixot --> sima matrix
		num = 0
		matrix_transp = [[0 for x in range(self.m)] for y in range(self.n)]
		for i in range(self.m):
			for j in range(self.n):
				matrix_transp[j][i] = self.werte[num]
				num += 1
		return matrix_transp

# Print transposed matrix
	def print_transp(self):
		print(self.transp_csak())

# Create a new object of class with transpose matrix
	def transp(self):
		werte_tr = []
		for i in range(self.n):
			for j in range(self.m):
				werte_tr.append(self.matrix[j][i])
		return Matrix(self.n, self.m, werte_tr)

# Overload __add__ --> create a new object of class for matrix_1+matrix_2
	def __add__(self,other):
		self.check_add(other)
		werte_add = [0 for x in range(len(self.werte))]
		for i in range(len(self.werte)):
			werte_add[i] = self.werte[i] + other.werte[i]
		add_matrix = self.erstellen_matrix(werte_add)
		return Matrix(self.m,self.n,werte_add)

# Overload __sub__ --> create a new object of class for matrix_1-matrix_2
	def __sub__(self,other):
		self.check_add(other)
		werte_sub = [0 for x in range(len(self.werte))]
		for i in range(len(self.werte)):
			werte_sub[i] = self.werte[i] - other.werte[i]
		sub_matrix = self.erstellen_matrix(werte_sub)
		return Matrix(self.m,self.n,werte_sub)

# Overload __mul__ --> create a new object of class for matrix_1*matrix_2
	def __mul__(self,other):
		self.check_mul(other)
		werte_mul = []
		for i in range(self.m):
			for j in range(other.n):
				tmp = 0
				for k in range(self.n):
					tmp += self.matrix[i][k]*other.matrix[k][j]
				werte_mul.append(tmp)
		return Matrix(self.m,other.n,werte_mul)

# Calculate determinat of matrix
	def det(self,A=""):
		self.check_squere()
		if A == "":
			A = self.matrix
		x = 0
		if len(A) == 1:
			x = A[0]
		elif len(A) == 2:
			x = A[0][0]*A[1][1]-A[0][1]*A[1][0]
		else:
			for i in  range(len(A)):
				x += (-1)**(0+i)*A[0][i]*self.det(self.remove_ij(A,0,i))
		return x

# auxiliary function for determinat (remove row and column)
	def remove_ij(self,A,m,n):
		A_ = [[0 for i in range(len(A[0])-1)]for j in range(len(A)-1)]
		si = 0
		for i in range(len(A_)):
			sj = 0
			if i == m:
				si = 1
			for j in range(len(A_[0])):
				if j == n:
					sj = 1
				A_[i][j] = A[i+si][j+sj]
		return A_

# Check input (m,n,werte)
	def check_nmw(self):
		if self.m*self.n != len(self.werte):
			print(self.w,"n,m,w")

# Check input (matrix)
	def check_mat(self):
		if type(self.mat) != list:
			print(self.w,"matrix")

		for i in range(len(self.mat)-1):
			for j in range(i+1,len(self.mat)):
				if len(self.mat[i]) != len(self.mat[j]):
					print(self.w,"matrix")

# Check input (addition)
	def check_add(self,other):
		if self.m != other.m or self.n != other.n:
			print(self.w,"addition")

# Check m1,n1,m2,n2 for multiplicatio
	def check_mul(self,other):
		if  self.m != other.n or self.n != other.m:
			print(self.w,"multiplication")
		
# Check squere
	def check_squere(self):
		if self.m != self.n:
			print(self.w,"squere")

# Print matrix clear for integer
	def print_clear_int(self):
		A = self.matrix
		S = [[0 for i in range(len(A[0]))] for j in range(len(A)+1)]
		for j in range(self.n):
			for i in range(self.m):
				S[i][j] = len(str(A[i][j]))
				if i == 0:
					S[-1][j] = S[i][j]
				elif S[i][j] > S[-1][j]:
					S[-1][j] = S[i][j]
		for i in range(self.m):
			s=""
			for j in range(self.n):
				if j != 0:
					s += "  "
				s += (1+S[-1][j]-S[i][j])*" "
				s += str(A[i][j])
			print(s)

# Print matrix clear for decimal
	def print_clear_dec(self):
		A = self.matrix
		Sint = [[0 for i in range(len(A[0]))] for j in range(len(A)+1)]
		Sdec = [[0 for i in range(len(A[0]))] for j in range(len(A)+1)]
		for j in range(self.n):
			for i in range(self.m):
				Sint[i][j] = len(str(int(A[i][j])))
				Sdec[i][j] = len(str(A[i][j]))-Sint[i][j]
				
				if i == 0:
					Sint[-1][j] = Sint[i][j]
				elif Sint[i][j] > Sint[-1][j]:
					Sint[-1][j] = Sint[i][j]
				
				if i == 0:
					Sdec[-1][j] = Sdec[i][j]
				elif Sdec[i][j] > Sdec[-1][j]:
					Sdec[-1][j] = Sdec[i][j]

		for i in range(self.m):
			s=""
			for j in range(self.n):
				if j != 0:
					s += "  "
					s += (Sdec[-1][j-1]-Sdec[i][j-1])*" "
				s += (1+Sint[-1][j]-Sint[i][j])*" "
				s += str(A[i][j])					
			print(s)

# Testfunction
def test():
	m = 2
	n = 3
	werte_1 = [11,12,13,21,22,23]
	m_1 = Matrix(m, n, werte_1)
	m_1_tr = m_1.transp_csak()
	print(type(m_1_tr))
	m_1_tr = m_1.transp()
	print(type(m_1_tr))
	m_1.print_matrix()
	m_1.print_transp()	# csak egy matrix nem Klasse ez*
	print(m_1_tr)		# __str__-re kiirja, __str__ nelkul csak a tipusat irna ki, hogy Klasse
	m_1.print_matrix()	# * nem modositotta ez eredeti Obj-ot
	print(m_1)			# __str__-re kiirja, __str__ nelkul csak a tipusat irna ki, hogy Klasse
	print(type(m_1))
	print("---\n")

	werte_2 = [23,22,21,13,12,11]
	m_2 = Matrix(m, n, werte_2)
	m_2.print_matrix()
	print(m_2)
	print("---\n")

	print(m_1 + m_2)
	m_3 = m_1 + m_2
	print(m_3)
	print("---\n")

	print(m_3 - m_2 - m_1)
	m_4 = m_3 - m_2 - m_1
	print(m_4)
	print("---\n")

	m_4 = m_1
	print((m_4+m_4+m_4).transp())
	print("---\n")

	m = [[11,22,33],[44,55,66]]
	m_5 = Matrix(m)
	print(m_5)
	print("---\n")

	werte_3 = [1,2,3,4,5,6]
	m_3 = 2
	n_3 = 3
	M_3 = Matrix(m_3,n_3,werte_3)
	print(M_3)
	werte_4 = [1,4,2,5,3,6]
	m_4 = 3
	n_4 = 2
	M_4 = Matrix(m_4,n_4,werte_4)
	print(M_4)
	print(M_3 * M_4)
	print("---\n")

	M_5 = [[1,2,3],[0,2,4],[1,3,3]]
	print(type(M_5))
	M_5 = Matrix(M_5)
	print(type(M_5))
	print(M_5.det())
	M_5.print_clear_int()
	print("---\n")

	M_6 = [[1.0,2,4444],[0.02,2.22,4],[1,3,3.33]]
	print(type(M_6))
	M_6 = Matrix(M_6)
	print(type(M_6))
	print(M_6.det())
	print()
	M_6.print_clear_int()
	print()
	M_6.print_clear_dec()
	print("---\n")

if __name__ == "__main__":
	test()
