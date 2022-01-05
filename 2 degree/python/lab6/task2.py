# Модифікований метод Ейлера

from numpy.lib.scimath import log 

def func(x, y):
	return (1-y+log(x))/x

def y1func(x, y, h):
	return y + h*func(x,y)

def yfunc(x, y, h):
	return y + 0.2/2 * (func(x, y) + func(x+h, y1func(x, y, 0.2)))

def ffunc(x, y, h):
	#print(" f = ", func(x,y), "f1 = ", round(func(x+h, y1func(x, y, 0.2)),3))
	#print(" x+h = ", x+h, " x = ", x, " y = ", y, " h = ", h)
	return 0.1/2 * (func(x,y) + func(x+h, y1func(x, y, 0.2)))

def Eluer_Cauchy(x, y, h, start, end):
	ar = []
	while round(start,1) <= end:
		ar.append(y) 
		if round(start,1) < end:
			print("x = ", x, " y = ", y, " f = ", round(func(x,y),3), " y1 =", round(y1func(x, y, 0.2),3),
				" f1 = ", round(func(x+h, y1func(x, y, 0.2)),3), 
				" ff = ", round(ffunc(x, y, h),3))  
			y = round(yfunc(x, y, h),3)
			start+=h
			x = round(start,3)
		else:
			#y = round(y + ffunc(x, y, h),3)
			print("x = ", x, " y = ", y)
			start+=h
	return ar

def efunc(y1, y2):
	i = len(y1) - 1
	ny1 = [l for l in range(1, len(y1))]
	ny2 = [l for l in range(2, len(y2), 2)]
	print(i)
	print(ny1)
	print(ny2)
	e = []
	for l in range(i):
		e.append(round(y2[ny2[l]] - y1[ny1[l]], 3))
	return e

x = 1
y = 1
h = 0.1
start = 1.0
end = 2.0

#print(efunc(Eluer_Cauchy(x, y, h, start, end), Eluer_Cauchy(x, y, 0.1, start, end)))
#print(h/2)
print(Eluer_Cauchy(x, y, h, start, end))
#print(Eluer_Cauchy(x, y, 0.1, start, end))