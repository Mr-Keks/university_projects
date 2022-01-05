from math import cos, sin
from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Method", "result"]

#Task 1
print("\t*****Iteration method*****")
x = float(input("Enter the initial approximation: "))
x1 = cos(x) #formula
e = float(input("Enter the accuracy: "))

while abs(x - x1) >= e:
	x = x1
	x1 = cos(x)
	
#Task 2
print("\n\t******Tangent method******")
y = float(input("Enter the initial approximation: "))
fy = y - cos(y)
ffy = 1 + sin(y)
y1 = y - (fy / ffy)

while  abs(y - y1) > e:

	y = y1
	fy = y - cos(y)
	ffy = 1 + sin(y)
	y1 = y - (fy / ffy)

#Task 3
print("\n\t******Bisection method*****")
c = float(input("Enter the initial approximation: "))
fa = 1.5 - cos(1.5)
fc = c - cos(c)
c1 = c - fc * (1.5 - c) / (fa - fc)


while abs(c1 - c) >= e:
	c = c1
	fa = 1.5 - cos(1.5)
	fc = c - cos(c)
	c1 = c - fc * (1.5 - c) / (fa - fc)

table.add_row(["iteration", round(x1, 5)])
table.add_row(["tangent", round(y1, 5)])
table.add_row(["bisection", round(c1, 5)])

print(table)
