from numpy.lib.scimath import log 


#Eyler
def function(x, y):
	return (1-y+log(x))/x

def Eluer(x, y, h, start, end):
	ar = []
	while round(start, 1) <= end:
		ar.append(y)
		if round(start, 1) < end:
			print("x = ", x, " y = ", round(y, 3), " f = ", 
				round(function(x,y), 3), 
				" hf = ", round(0.1 * function(x,y), 3))
			y = round(y + 0.1 * function(x,y), 3)
			start+=h
			x = round(start, 1)
		else:
			x = round(start, 1)
			print("x = ", x, " y = ", round(y, 3))
			start+=h
	return ar

def eFunc(y1, y2):
	i = len(y1) - 1
	ny1 = [l for l in range(1, len(y1))]
	ny2 = [l for l in range(2, len(y2), 2)]
	e = []
	for l in range(i):
		e.append(round(y2[ny2[l]] - y1[ny1[l]], 3))
	return e 	

x = 1.0
y = 1.0
e = 0
h = 0.1
i = 1
end = 2.0
Eluer(x, y, h , i, end)