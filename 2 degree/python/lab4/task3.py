# Методі Сімпсона

from math import cos

m1 = float(input("first point: "))
m2 = float(input("second point: "))

h1 = 0.1
h2 = h1 * 2

def func1(x):
	return cos(x**2) / (x+1)

def cikle(h):
	x = m1 
	xd = func1(x)
	fxd = xd
	lxd = 0
	suma = 0
	while x <= m2:
		x+=h
		lxd = xd
		xd = func1(x)
		suma += xd
	return suma-xd, fxd+lxd

s, g = cikle(h1)
s1, g = cikle(h2)
g = g/2
print("suma = ", s+g, " integral in h1 = ", (s+g) * h1)
print("suma = ", s1+g, " integral in h2 = ", (s1+g) * h2)
print("pohibka = ", abs((s+g) * h1 - (s1+g) * h2 )/3)