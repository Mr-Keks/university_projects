#Метод Ньютона:

def filling_array(k):
	x = []
	for i in range(k):
		x.append(float(input(f"Enret {i} value: ")))
	return x

def rek(x, n, k):

    if k == len(x)-2:
    	return x[n+1] - x[n]
    else:
    	return rek(x, n+1, k+1) - rek(x, n, k+1)

def fact(x):
	if x == 0:
		return 1
	else:
		return x * fact(x-1)

def mx(ox, x, n):
	if n == 0:
		return ox - x[n]
	else:
		return (ox - x[n]) * mx(ox, x, n-1)


def p_func(x, y, n, k, ox, c, h=1):
	if n == len(y)-1:
		return (rek(y, 0, k) * mx(ox, x, c) / (fact(n)*h**n))
	else:
		return (rek(y, 0, k)*mx(ox, x, c) / (fact(n) * h**n)) + p_func(x, y, n+1,  k-1, ox, c+1, h)

r = 5
print("*****Filling array x: ")
x = filling_array(r)
print("\n*****Filling array y: ")
y = filling_array(r)
ox = float(input("\nEnter argument: "))
h = x[1]-x[0]


print("result = ", y[0]+p_func(x, y, 1, 3, ox, 0, h))
