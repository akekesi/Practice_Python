# Integral (Riemann, Monte-Carlo)

import random
import matplotlib.pyplot as plt

# Randomwerte
def funk_rand():
	r = []
	x = []
	for i in range(1001):
		r.append(random.uniform(0,100))
		x.append(i)
	plt.scatter(x,r)
	plt.title('Random-Punkte', fontsize=16)
	plt.show()

# Riemannsche Zwischensumme
def funk_riemann_zws(von, bis, step, funk, *args, **kwargs):
	f = []
	x = []
	xr = []
	integral = 0
	for i in range(int((bis-von)/step)):
		tmp = von + i*step
		x.append(tmp)
		tmp = random.uniform(tmp,tmp+step)
		xr.append(tmp)
		f.append(funk(tmp,*args, **kwargs))
		integral += f[i] * step
	print("Integral: "+str(rund(integral,2)))
	plt.plot(x,f,marker='.',markersize=10,label='original x')
	plt.plot(xr,f,marker='.',markersize=10,label='Stuetzpunkt')
	plt.title('Riemannsches Integral', fontsize=16)
	plt.legend()
	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid()
	plt.show()

# Monte-Carlo Integral
def funk_monte_carlo_integral(von_x, bis_x, step_x, von_y, bis_y, step_y, funk, *args, **kwargs):
	f = []
	x = []
	f_u_p = []
	x_u_p = []
	f_u_n = []
	x_u_n = []
	f_o = []
	x_o = []
	sum_u_p = 0
	sum_u_n = 0
	sum_o = 0
	A = (bis_x-von_x)*(bis_y-von_y)
	r_x = int((bis_x-von_x)/step_x)+1					# ? +1 or not ?
	r_y = int((bis_y-von_y)/step_y)+1					# ? +1 or not ?
	for i in range(r_x):
		f.append([])
		x.append([])
		for j in range(r_y):
			tmp_x = von_x + i*step_x
			x[i].append(tmp_x)
			tmp_y = random.uniform(von_y, bis_y)		# Random:  von <= x < bis
			f[i].append(tmp_y)
			if tmp_y <= funk(tmp_x) and tmp_y >= 0:
				f_u_p.append(tmp_y)
				x_u_p.append(tmp_x)
				sum_u_p += 1
			elif tmp_y >= funk(tmp_x) and tmp_y <= 0:
				f_u_n.append(tmp_y)
				x_u_n.append(tmp_x)
				sum_u_n += 1
			else:
				f_o.append(tmp_y)
				x_o.append(tmp_x)
				sum_o += 1
	print("Alle Punkte: "+str(int(r_x*r_y)))
	print("Unter pos.:  "+str(sum_u_p))
	print("Unter neg.:  "+str(sum_u_n))
	print("Obern:       "+str(sum_o))
	print("Integral:    "+str(A/(r_x*r_y)*(sum_u_p-sum_u_n)))
				
	#plt.eventplot(f,linelengths=0.05, orientation='vertical')

	fig,axs = plt.subplots(1,4)
	axs[0].scatter(x, f, marker='.')
	axs[0].set_title('alle Punkte')
	axs[1].scatter(x_u_p, f_u_p, c='r', marker='.')
	axs[1].set_title('unten pos.')
	axs[2].scatter(x_u_n, f_u_n, c='b', marker='.')
	axs[2].set_title('unten neg.')
	axs[3].scatter(x_o, f_o, c='g', marker='.')
	axs[3].set_title('oben')
	fig.suptitle("Monte-Carlo Integral", fontsize=16)
	plt.show()

# Hilfsfunktion x**n
def xhochn(x,n):
	return x**n

# Hilfsfunktion x**5-5*x**3
def testfunk(x):
#	return x**2
	return x**5-5*x**3

# Hilfsfunktion runden
def rund(x,n):
	r_1 = round(x,n)
	r_2 = int(x*10**n+0.5)/10**n
	if r_1 == r_2:
		return r_2
	else:
		print("Fehler!")

if __name__ == "__main__":
	funk_rand()
	print("---")
	funk_riemann_zws(0, 3, 0.1, xhochn,2)
	print("---")
	funk_monte_carlo_integral(-2, 2, 0.01, -13, 13, 0.1, testfunk)
