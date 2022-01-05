# Метод Ругне-Кутта

from prettytable import PrettyTable
from math import exp
from numpy.lib.scimath import logn as ln
from math import e

table = PrettyTable()
table.field_names = ["x", "y", "k1", "k2", "k3", "k4", "dy"]

def func(x, y):
	return x**2 - 2*y
	

def k_func(y, x, h):
	k = [func(x, y)]
	for i in range(2):
		k.append(func(x + h/2, y + h*k[i]/2))
	k.append(func(x+h, y+h*k[2]))
	return k

def filling_x(h, xk, x0):
	x = [x0]
	for i in range(int((xk-x[0])/h)):
		x.append(x[i]+h)
	return x

def suma_k(k):
	suma = k[0]
	for i in range(2):
		suma += 2*k[i+1]
	suma += k[3]
	return suma

def dy(h, k):
	return h/6*(suma_k(k))

def ddk(k):
	return abs( (k[1]-k[2]) / (k[0]-k[1]) )
h=0.1
y0 = 1
x0 = 0
xk = 1
dk = []
x = filling_x(h, xk, x0)
print(len(x))
y = [y0]
d = []

for i in range(11):
	k = k_func(y[i], x[i], h)
	d.append(dy(h, k))
	table.add_row(
	[
		float(f'{x[i] :.6f}'), 
		float(f'{y[i]:.6f}'),
		float(f'{ k[0]:.6f}'), 
		float(f'{ k[1]:.6f}'), 
		float(f'{ k[2]:.6f}'), 
		float(f'{ k[3]:.6f}'), 
		float(f'{ d[i]:.6f}')
	])
	dk.append(ddk(k))
	dk[i] = float(f'{dk[i]:.3f}')
	y.append(y[i] + d[i])
print(table)
print(dk)