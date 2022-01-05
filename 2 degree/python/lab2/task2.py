from math import cos, sin
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Method", "result"]

B = float(input("Enter the B value: "))
C = float(input("Enter the C value: "))
D = float(input("Enter the D value: "))
e = float(input("Enter the accuracy: "))



#Task 1
print("\t*****Iteration method*****")

x = float(input("Enter the initial approximation: "))
x1 = 1 


while abs(x - x1) > e:
	x = x1
	x1 = D/(x**2-B*x+C)
print(round(x1,5))
	
#Task 2
print("\n\t******Tangent method******")


y = float(input("Enter the initial approximation: "))
fy =  y**3 - B*y**2 + C*y - D
ffy = 3*y**2 - 2*B*y + C
y1 = y - (fy / ffy)

while  abs(y - y1) > e:

	y = y1
	fy =  y**3 - B*y**2 + C*y - D
	ffy = 3*y**2 - 2*B*y + C
	y1 = y - (fy / ffy)

print(round(y1,5))

#Task 3
print("\n\t******Bisection method*****")


b = float(input("Enter the initial approximation: "))
a = -2
fb = b**3 - B*b**2 + C*b - D
fa = a**3 - B*a**2 + C*a - D
c = a - ((fa * (b - a)) / (fa - fb))
c1 = 1000

while abs(c1 - c) > e:
	c = c1
	fc = c**3 - B*c**2 + C*c - D
	fb = b**3 - B*b**2 + C*b - D
	c1 = c - (((c-b)*(fc)) / (fc-fb))
print(round(c1,5))

table.add_row(["iteration", round(x1, 5)])
table.add_row(["tangent", round(y1, 5)])
table.add_row(["bisection", round(c1, 5)])

print(table)
