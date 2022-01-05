# Удосконалений метод Ейлера

from prettytable import PrettyTable
from numpy.lib.scimath import logn as ln
from math import e

table = PrettyTable()
table.field_names = [
		"x", 
		"y", 
		"x+h/2", 
		"f(x,y)", 
		"y+h*f(x,y)/2", 
		"f(x+h/2, y+h*f(x,y)/2", 
		"dy"
	]

def func(x, y):
	return x**2 - 2*y

def filling_x(h, xk, x0):
	x = [x0]
	for i in range(int((xk-x[0])/h)):
		x.append(x[i]+h)
	return x

def dy(h, x, y):
	return h * func(x, y)

x0 = 0
y0 = 1
xk = 1

h = 0.1
y = [y0]
x = filling_x(h, xk, x0)

#print(x[0]+h/2)
#print(func(x[0], y[0]))
#print(y[0]+(h*func(x[0],y[0]))/2)
#print(func(x[0]+h/2, y[0]+(h*func(x[0],y[0]))/2))
#print(dy(h, x[0], y[0]))

for i in range(len(x)):
	z = x[i]+h/2
	d = y[i]+(h*func(x[i],y[i]))/2
	table.add_row([	float(f'{x[i]:.1f}'), float(f'{y[i]:.5f}'),	float(f'{z:.5f}'),	
		float(f'{func(x[i], y[i]):.5f}'), 
		float(f'{d:.5f}'), 
		float(f'{func(z, d):.5f}'), 
		float(f'{dy(h,z,d):.5f}')])
	y.append(y[i]+dy(h,z,d))
print(table)
