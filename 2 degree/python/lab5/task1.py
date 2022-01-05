# Метод прямокутників

from math import cos

h1 = 0.1
h2 = h1 * 2
m1 = float(input("first point: "))
m2 = float(input("second point: "))

def func1(x):
	return cos(x**2) / (x+1)

def cikle(h):
	x = m1+h
	xp = m1
	xd = 0
	xc = 0
	suma = 0
	while xp <= m2:
		xc = (xp + x) / 2
		xd = func1(xc)
		suma += xd
		xp = x
		x+=h
	return suma-xd

s = cikle(h1)
s1 = cikle(h2)

print("suma = ", s, " doubutok = ", s * h1)
print("suma = ", s1, " doubutok = ", s1 * h2)
print("pohibka = ", abs(s1 * h2 - s * h1)/3)
