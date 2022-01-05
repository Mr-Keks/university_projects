# Метод трапеції

from math import cos

m1 = float(input("first point: "))
m2 = float(input("second point: "))

h1 = 0.1
h2 = h1*2

def func1(x):
	return cos(x**2) / (x+1)

def cikle(h):
	x = m1
	xc = 0
	xe = 0
	n = 2
	suma = 0
	i = 2

	def c(x, h):
		res = 0
		for i in range(3):
			xe = func1(x)
			if i == 1:
				xe *= 4
			res += xe 
			x += h
		return res

	while x <= m2:
		xc = func1(x)
		if n <= (1/h) and n % 2 == 0 and n != 1 and x != m2:
			xe = (h/3) * c(x, h)
			suma += xe
		x+=h
		n+=1.0
		i+=1
	return suma
	
print("suma h1 = ", cikle(h1))
print("suma h2 = ", cikle(h2))
print("pohibka = ", abs(cikle(h1) - cikle(h2)) / 15)