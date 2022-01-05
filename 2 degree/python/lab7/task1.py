from array import * 
import math  

a = 0
b = 1 
n=6 
h = float((b-a)/(n-1)) 
x = [0]*n 
for i in range(1,len(x)): 
	x[i]=x[0]+i*h 
def k1():
	k = []
	for i in range(n):
		k.append([])
	for i in range(n):
		for j in range(n):
			k[i].append(0)
	return k

def func(koef, x, h):
	def func1(i, koef, x, h):
		koef[i][i+2] = 1 + h/(x[i+2]-2)
		koef[i][i+1] = (h**2)*(x[i+1]-2) - 2 
		koef[i][i] = 1 + h/(x[i]-2)
		return koef
	def func2(i, koef, x, h):
		koef[i][i+1] = 1 + h/(x[i+1]-2)
		koef[i][i] = (h**2)*(x[i]-2) - 2 
		koef[i][i+2] = 1 + h/(x[i+2]-2)
		return koef
	def func3(i, koef, x, h):
		koef[i][i] = 1 + h/(x[i]-2) 
		koef[i][i+2] = (h**2)*(x[i+2]-2) - 2 
		koef[i][i+1] = 1 + h/(x[i+1]-2)
		return koef
	for i in range(4):
		for j in range(4):
			if i == 0 or i == 3:
				func1(i, koef, x, h)	 
			if i == 1:
				func2(i, koef, x, h)
			if i == 2: 
				func3(i, koef, x, h)

 

	koef[5][5] = b[0]*h/2 + b[1]/2 
	koef[5][4] = (-1)*b[1]/2 
	koef[4][1] = a[1] 
	koef[4][0] = a[0]*h - a[1] 
	return koef

koef = k1()  

def haus(koef, y, f):
	k = 0 
	i = 1 
	j = 0 

	while k < 5: 
		while i <= 5: 
			l = 0 
			j = 0 
			l = koef[i][k]/koef[k][k] 
			f[i] = f[i] - l*f[k] 
			while j <= 5: 
				koef[i][j] = koef[i][j] - l*koef[k][j] 
				j+=1 
			i+=1 
		k+=1 
		i=k+1 
		j=k 

	y[5]=f[5]/koef[5][5] 
	i=4 

	while i >= 0: 
		y[i]=f[i] 
		j=i+1 
		while j <= 5:
			y[i]=y[i]-(koef[i][j])*y[j] 
			j+=1 
		y[i]=y[i]/koef[i][i] 
		i=i-1 

	print('Результат: ') 
	for i in range(6):
		print('y[',i,']', y[i]) 

def p0(koef, x, h):
	def f1(koef, x, h):
		koef[ i ][ i+1 ] = 1 + h/(x[i+1]-2) 
		koef[ i ][ i ] = (h**2)*(x[i]-2) - 2 
		koef[ i ][ i-1 ] = 1 + h/(x[i-1]-2) 
		return koef
	def f2(koef, x, h):
		koef[ i ][ i ] = 1 + h/(x[i]-2) 
		koef[ i ][ i-1 ] = (h**2)*(x[i-1]-2) - 2 
		koef[ i ][ i+1 ] = 1 + h/(x[i+1]-2) 
		return koef
	def f3(koef, x, h):
		koef[ i ][ i-1 ] = 1 + h/(x[i-1]-2) 
		koef[ i ][ i+1 ] = (h**2)*(x[i+1]-2) - 2 
		koef[ i ][ i ] = 1 + h/(x[i]-2) 
		return koef
	for i in range(1,5): 
		for j in range(1,5): 
			if i == 1 or i == 4: 
				f1(koef, x, h)
			if i == 2: 
				f2(koef, x, h)
			if i == 3: 
				f3(koef, x, h)

	koef[ 5 ][ 5 ] = b[0]*h/2 + b[1]/2 
	koef[ 5 ][ 4 ] = (-1)*b[1]/2 
	koef[ 0 ][ 1 ] = a[1] 
	koef[ 0 ][ 0 ] = a[0]*h - a[1] 
	return koef

def pm1(A, B, koef):
	for i in range(5): 
		if i == 0: 
			A[i]=-koef[i][i+1]/koef[i][i] 
			B[i]=f[i]/koef[i][i] 
		else: 
			s = (koef[i][i-1]*A[i-1] + koef[i][i+1]) 
			A[i]=-koef[i][i]/s 
			B[i]=(f[i]-koef[i][i-1]*B[i-1])/s 
	return A, B
def pm2(A, B, y1):
	for i in range(4,0,-1): 
		y1[i-1]=A[i-1]*y1[i]+B[i-1] 
		print('y1[', i ,']',y1[i]) 
	return y1
def p(y1, y):
	for i in range(1,5):
		e = math.fabs(y1[i]-y[i]) 
		print('e[', i ,']',e) 
y = [0]*n 
f = [0.04,0.04,0.04,0.04,-0.1,-0.1] 
a = []
b = []

a.append(1) 
a.append(0)
a.append(-0.5)

b.append(1)
b.append(0)
b.append(-1) 

print("**Скінченно-різницевий метод**")

koef = func(koef, x, h)


for i in range(len(koef)): 
	for j in range(len(koef[i])): 
		print(koef[i][j], end = " ") 
	print() 
print() 

print("**Розв'язування методом Гаусса**")
haus(koef, y, f)

print("**Метод прогонки**") 

koef = k1()  
for i in range(n):
	for j in range(n):
		koef.append(0)

for i in range(1,5):
	for j in range(1,5): 
		if i == 1 or i == 4: 
			koef[ i ][ i+1 ] = 1 + h/(x[i+1]-2) 
			koef[ i ][ i ] = (h**2)*(x[i]-2) - 2 
			koef[ i ][ i-1 ] = 1 + h/(x[i-1]-2) 
		if i == 2: 
			koef[ i ][ i ] = 1 + h/(x[i]-2) 
			koef[ i ][ i-1 ] = (h**2)*(x[i-1]-2) - 2 
			koef[ i ][ i+1 ] = 1 + h/(x[i+1]-2) 
		if i == 3: 
			koef[ i ][ i-1 ] = 1 + h/(x[i-1]-2) 
			koef[ i ][ i+1 ] = (h**2)*(x[i+1]-2) - 2 
			koef[ i ][ i ] = 1 + h/(x[i]-2) 

koef[ 5 ][ 5 ] = b[0]*h/2 + b[1]/2 
koef[ 5 ][ 4 ] = (-1)*b[1]/2 
koef[ 0 ][ 1 ] = a[1] 
koef[ 0 ][ 0 ] = a[0]*h - a[1] 

 

A=[0]*n 
B=[0]*n 
y1 = [0]*n 
f = [-0.1,0.04,0.04,0.04,0.04,-0.1] 
e=0 
s=0 
koef = k1()
koef = p0(koef, x, h)
A, B = pm1(A, B, koef)

y1[4]=B[4]	 
print('Результат: ') 
y1 = pm2(A, B, y1)
print('Похибка: ') 
p(y1, y)
