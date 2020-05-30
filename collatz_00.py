# Collatz-Conjecture Analysis
# different sorters/plots/prints

from matplotlib import pyplot as plt
from matplotlib import animation
from celluloid import Camera 

# Collatz-Path from x to 1
def collatz(x):
	x_list = []
	x_list.append(x)
	while x != 1:
		if x%2 == 0:
			x = x/2
		else:
			x = x*3+1
		x_list.append(int(x))
	return x_list

# All Collatz-Path with lenght n
def collatz_back(n):
	a = [1]
	A = [a]
	while len(A[0]) != n:
		for i in range(len(A)):
			if (A[i][-1]-1)%3 == 0 and A[i][-1]-1 != 0:
				tmp = A[i].copy()							# without copy() would be just a reference and also A[i] would be overwitten 
				tmp.append(int((A[i][-1]-1)/3))
				A.append(tmp)
			A[i].append(A[i][-1]*2)
	return A

# All Collatz-Path with lenght n (with details)
def collatz_back_details(n):
	a = [1]
	A = [a]

	print("Increment of length/number of paths:")
	while len(A[0]) != n:									# All Collatz-Path
		print("#Path: "+str(len(A))+" --> "+str(A))			# Print increment of length/number of paths (1/2)
		for i in range(len(A)):
			if (A[i][-1]-1)%3 == 0 and A[i][-1]-1 != 0:
				tmp = A[i].copy()							# without copy() would be just a reference and also A[i] would be overwitten 
				tmp.append(int((A[i][-1]-1)/3))
				A.append(tmp)
			A[i].append(A[i][-1]*2)
	print("#Path: "+str(len(A))+" --> "+str(A))				# Print increment of length/number of paths (2/2)
	return A

# Sort Collatz-Paths from last element
def collatz_sort_1(A):
	j = len(A[0])-1
	s = 0
	while j > 3:
		for i in range(s+1,len(A)):
			if A[i][j] == A[s][j]:
				tmp = A[s+1]
				A[s+1] = A[i]
				A[i] = tmp
				s += 1
		j -= 1
	return A

# Sort Collatz-Paths from first element
def collatz_sort_2(A,row=0,AE=""):
	if AE == "":
		a = 0
		e = len(A)
	else:
		a = AE[0]
		e = AE[1]

	for j in range(a,e-1):				# sort increasing
		for i in range(j+1,e):
			if A[j][row] < A[i][row]:
				tmp = A[j]
				A[j] = A[i]
				A[i] = tmp

	tmp = [a]							# check repeating values --> next row sorted increasing
	for i in range(a+1,e):
		if A[i-1][row] == A[i][row]:
			tmp.append(i)
			if i == e-1:
				a1 = tmp[0]
				e1 = a1+len(tmp)
				AE = [a1,e1]
				A = collatz_sort_2(A,row+1,AE)
		elif A[i-1][row] != A[i][row] and len(tmp) == 1:
			tmp = [i]
		elif A[i-1][row] != A[i][row] and len(tmp) > 1:
			a2 = tmp[0]
			e2 = a2+len(tmp)
			AE = [a2,e2]
			A = collatz_sort_2(A,row+1,AE)
			tmp = [i]
	return A

# Sort Collatz-Paths (reverse)
def collatz_sort_rev(A):
	length = len(A)
	tmp = []
	for i in range(length-1,-1,-1):
		tmp.append(A[i])
	A = tmp
	return A

# Print Collatz-Paths
def collatz_print(A,txt=""):
	print("\nCollatz-Paths ("+txt+"):")
	m = len(str(max(map(max,A))))		# map(max,A) --> list of (max of A[i])
	for i in range(len(A)):
		tmp = ""
		for j in range(len(A[0])):
			space = (m+1-len(str(A[i][j])))*" "
			tmp += space+str(A[i][j])
		print(tmp)
	return A

# Number of Collatz-Path depend on length
def collatz_pathsnumber(A):
	S = []
	for i in range(len(A[0])):
		L = []
		for j in range(len(A)):
			L.append(A[j][i])
		S.append(variant(L))
	return S

# List contains x s-times
def list_contain(L,x):
	s = 0
	for i in range(len(L)):
		if type(L[i]) == list:
			s += list_contain(L[i],x)
		else:
			if x == L[i]:
				s += 1
	return s

# Number of different elements of list
def variant(L):
	S = 0
	while len(L) != 0:
		L0 = L[0]
		s = 0
		for i in range(len(L)):
			if L0 == L[i]:
				s += 1
		for i in range(s):
			L.remove(L0)
		S += 1
	return S

# Plot & Print Length of Collatz-Path and Collatz-Paths
def collatz_plot(n1=1001,n2=10):
	fig, axs  = plt.subplots(1,2)
	fig.suptitle("Collatz-Conjecture",fontsize=16)
	collatz_list = [0]
	collatz_list_lenght = [0]
	for i in range(1,n1):
		A = collatz(i)
		collatz_list.append(A)
		collatz_list_lenght.append(len(A))
	axs[0].bar(range(n1),collatz_list_lenght)
	axs[0].set_xlabel('Initial Value')
	axs[0].set_ylabel('Lenght of Collatz-Path')
	axs[0].set_title('Length of Collatz-Path')
	axs[0].grid(True)

	A0 = collatz_back_details(n2)
	collatz_print(A0,"original")
	A1 = collatz_sort_1(A0)
	collatz_print(A1,"sorted-1")
	A2 = collatz_sort_2(A0)
	collatz_print(A1,"sorted-2")
	A2 = collatz_sort_rev(A2)
	collatz_print(A2,"sorted-reverse")
	for i in range(len(A2)):
		axs[1].plot(range(1,len(A2[i])+1),A2[i],marker='.',markersize=10)
	axs[1].set_xticks(range(0,n2+1,1))
	axs[1].set_xlabel('Length of Collatz-Path')
	axs[1].set_ylabel('Initial Value')
	axs[1].set_title('Collatz-Path')
	axs[1].grid(True)
	plt.show()

# Plot Collatz-Path with gif
def collatz_path_gif(n,filename="Collatz_Path.gif"):
	A = collatz(n)
	xt = [A[0],A[-1]]
	style = "arc3,rad=0.5"
	ms = 9
	mw = 2
	s2 = 0
	s3 = 0

	fig = plt.figure("Collatz-Path")
	ax = fig.add_subplot(1, 1, 1)
	cam = Camera(fig)
	print("Length of Collatz-Path of "+str(n)+": "+str(len(A)))
	for i in range(len(A)):
		for j in range(i):
			if j == 0:
				ax.plot(A[j],0,'kx',markersize=ms,markeredgewidth=mw)
			else:
				ax.plot(A[j],0,'k.',markersize=ms)
			if j > 0:
				ax.annotate("",
				xy=(A[j-1],0), xycoords='data',
				xytext=(A[j],0), textcoords='data',
				arrowprops=dict(arrowstyle="<-", color="k",
								shrinkA=5, shrinkB=5,
								patchA=None, patchB=None,
								connectionstyle=style,
								),
								)
		if i == 0:
			ax.plot(A[0],0,'rx',markersize=ms,markeredgewidth=mw)
		else:
			ax.plot(A[i],0,'r.',markersize=ms)
		if i > 0:
			if A[i-1] > A[i]:
				s2 += 1
			else:
				s3 += 1
			ax.annotate("",
			xy=(A[i-1],0), xycoords='data',
			xytext=(A[i],0), textcoords='data',
			arrowprops=dict(arrowstyle="<-", color="r",
								shrinkA=5, shrinkB=5,
								patchA=None, patchB=None,
								connectionstyle=style,
								),
								)
			if i != len(A)-1:
				xt.append(A[i])
		ax.set_xticks(xt)
		ax.tick_params(axis='x', colors="k")				
		ax.set_yticks([])
		ax.text(max(A)-1*int(max(A))/5,0.04,'x/2:'+'\nx*3+1:'+'\nsteps:')								# ? tabulator, or \t would be better ?
		ax.text(max(A)-0.3*int(max(A))/5,0.04,str(s2)+'\n'+str(s3)+'\n'+str(s2+s3)+'/'+str(len(A)-1))	# ? tabulator, or \t would be better ?
		ax.spines['left'].set_position('zero')
		ax.spines['right'].set_color('none')
		ax.spines['top'].set_color('none')
		ax.spines['bottom'].set_position('zero')
		ax.set_title('Collatz-Path')
		cam.snap()
	animation = cam.animate(interval=1500)
	animation.save(filename, writer = 'imagemagick')
	plt.show()

# Plot Collatz-Paths with gif
def collatz_paths_gif(n,filename='Collatz_Paths.gif'):
	A = collatz_back(n)
	A = collatz_sort_2(A)
	A = collatz_sort_rev(A)
	S = collatz_pathsnumber(A)
	col = int(10/len(A))/10
	fig = plt.figure("Collatz-Paths")
	cam = Camera(fig)
	for i in range(len(A[0])):
		for j in range(len(A)):
			plt.plot(range(1,i+2),A[j][:i+1],color=(j*col,j*col,j*col),marker='.',markersize=10)
		plt.xticks(range(0,n+1,1))
		plt.text(1,int(max(map(max,A))/3),'Number of Collatz-Paths: '+str(S[i]),fontsize=12)
		plt.xlabel('Lenght of Collatz-Path')
		plt.ylabel('Initial Value')
		plt.title('Collatz-Paths')
		plt.grid(True)
		cam.snap()
	animation = cam.animate(interval=1500)
	animation.save(filename, writer = 'imagemagick')
	plt.show()

if __name__ == "__main__":
	collatz_plot(1001,10)
	collatz_path_gif(13)
	collatz_paths_gif(9)
