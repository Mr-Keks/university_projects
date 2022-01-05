from math import cos, exp, sin
from prettytable import PrettyTable

def func1(x): 
	return cos(2*x - 0.7) - 0.3 * exp(0.5-x)
	
def func2(x, y):
	return cos((x + y)-0.7) - 0.3*exp(0.5-(x + y)/2)

a = float(input("Enter first limit: "))
b = float(input("Enter second limit: "))
e = float(input("Enter accuracy: "))

k = func2(a, b)
fa, fb = func1(a), func1(b)
i = 1

table = PrettyTable()
table.field_names = [
	"number of iteration", 
	"a", "b", "f(a)", "f(b)", 
	"f((b-a)/2)", "|a-b|"
	]

while abs(a-b) > e:
	table.add_row([i, float(f'{a :.9f}'), float(f'{b :.9f}'), fa, fb, k, abs(a-b)])
	if k*fa < 0:
		a = a	
	else:
		a = (a + b)/2
	if k*fb < 0:
		b = b
	else:
		b = (a+b)/2
	k = func2(a, b)
	fa = func1(a)
	fb = func1(b)
	i+=1
table.add_row([i, float(f'{a :.9f}'), float(f'{b :.9f}'), fa, fb, k, abs(a-b)])
print(table)
print("Answer = ", f'{(a+b)/2 :.9f}')
