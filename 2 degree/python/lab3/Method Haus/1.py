class Matrix():
	def __init__(self, rows, column):
		self.rows = rows
		self.column = column
		self.free_members = [rows]
		self.matrix = []
	

	def create_matrix(self):
		for i in range(self.rows):
			self.matrix.append(func(self.column, i))

	def show_matrix(self):
		print(self.matrix)

	
	def func(self):
		return self.matrix

def func(c, r):
	a = []
	for i in range(c):
		print("Enter", r , "rows and ", i, "column matrix value: ")
		a.append(input())
	return a

#function
 
def plus_matrix(matrix, column, the_column, b):
	i = the_column
	j = the_column
	start = the_column
	while i < column-1:
		the_column = start
		n = matrix[the_column+1][the_column]
		b[i+1] += b[start] * n
		while the_column < column:
			matrix[i+1][the_column] += matrix[i][the_column] * n
			the_column+=1
		i+=1
	return matrix
def minus_matrix(matrix, column, the_column, b):
	i = the_column
	j = the_column
	start = the_column
	while i < column-1:
		the_column = start
		n = matrix[i+1][the_column]
		b[i+1] -= b[start] * n
		while the_column < column:
			matrix[i+1][the_column] -= matrix[j][the_column] * n
			the_column+=1
		
		i+=1
	return matrix, b
def dil_matrix(matrix, the_rows, column, b):
	i = the_rows
	dil = matrix[the_rows][the_rows]
	while i < column:
		matrix[the_rows][i] /= dil
		i+=1
	b[the_rows] /= dil
	return matrix, b
def chek_matrix(matrix, rows, the_rows):
	a = the_rows
	res = matrix[the_rows][a]
	a1 = 0
	#while the_rows < rows-1:
	print("res = ", res, " m = ", matrix[the_rows+1][a])
	if res > matrix[the_rows+1][a]:
	#	res = matrix[the_rows+1][a]
	#	a1 = the_rows+1
	#	the_rows += 1
		a1 = the_rows+1	
	return a1

def change_place(matrix, the_rows, column, change_rows, b):
	temp = 0
	n = the_rows
	print("ch = ", change_rows)
	#print("t = ", the_rows)
	while the_rows < column:
		print("n = ", n)
		print("the rows = ", the_rows)
		temp = matrix[n][the_rows]
		matrix[n][the_rows] = matrix[change_rows][the_rows]
		matrix[change_rows][the_rows] = temp
		the_rows += 1
	temp = b[n]
	b[n] = b[change_rows]
	b[change_rows] = temp

	return matrix, b
'''
def find_result(a,b, rows):
	k = [0,0,0]
	res = 0
	rows -=1
	m = 0
	for i in range(rows, -1, -1):
		#print("new")
		#print("k = ", k)
		#print("a = ", a)
		#print("b = ", b)
		c = 0
		res = 0
		for j in range(rows, -1, -1):
			#print("j = ", a[i][j])
			#print("kc = ", k[c])
			if j != rows:
				if a[i][j] == 1:
					res += k[c]
				else:
					res += a[i][j] + k[c]
				c+=1
			else:
				res+=a[i][j]
		#	print("aij = ", a[i][j], " i = ", i, " j = ", j )
	#		print("aaa = ", a)
	#		print("res = ", res)
			
			
		
		
		#print("b[rows] = ", b[i])
		#print("res = ", res)
		if i == rows:
			k[m] = (b[i]/res)
		else:
			#print("bi = ", b[i], " res = ", res)
			k[m] =   b[i] - res 
		m+=1
	print(k)
	return k
'''

def find_result(a, b, rows):
	k = []
	rows -= 1
	temp = 0
	for i in range(rows, -1, -1):
		print(k)
		res = 0
		c = 0
		print("i = ", i)
		print()
		for j in range(rows, -1, -1):
			#print(a[i][j])
			#print(" k = ", k[c])
			#print(a[i][j] * k[c])
			try:
				print("res = ", res) 	
				print(" k = ", k[c])
				print("a = ", a[i][j])
				res += a[i][j] * k[c]
				c+=1
			except IndexError:
				if a[i][j] != 0:
					temp = a[i][j]
				break
				
		print("res = ", res)
		print("b = ", b[i])
		print("temp = ", temp)
		if i == rows:
			print("i in: ", i)
			k.append(float(f'{(b[i] / temp):.3f}'))
		else:
			k.append(float(f'{((b[i] - res) / temp):.3f}'))

	return k
column = 4
rows = 4
'''
a = Matrix(rows, column)
a.create_matrix()
a.show_matrix()

a = a.func()
for i in range(rows):
	for j in range(column):
		a[i][j] = int(a[i][j])
'''
#plus_matrix(a, column, k)
#minus_matrix(a, column, k)
#dil_matrix(a, k, column)
#change_place(a, k, column, chek_matrix(a, rows, k) + k)
#a = [[1,1,1], [1,-1,2], [2,-1,-1]]
#a = [[1,-2,3],[4,-1,5],[6,-8,7]]
#b = [6,5,-3]
#b = [2,15,9]
#a = [[4,3,-2], [1,2,1], [3,2,1]]
#b = [4,8,10]
a = [[1, -1, 7, 1], [3,1,-9,-4], [-1,5,-1,2],[2,-1,3,11]]
b = [-1,11,7,-16]


'''
for i in range(rows-1):
	print("i = ", i)
	if a[i][i] > a[i+1][i]:
		change_place(a, i, column, chek_matrix(a, rows, i), b)
	if a[i][i] != 1:
		dil_matrix(a, i, column, b)
	minus_matrix(a, column, i, b)

for i in range(rows):
	print("(", end = '')
	for j in range(column):
		print(a[i][j], ", ", end = '')
	print(")")
print(b)
print(find_result(a,b,rows))
'''
print(a)
print(b)

for i in range(rows-1):
	if chek_matrix(a, rows, i):
		change_place(a, i, column, chek_matrix(a, rows, i), b)
	if a[i][i] != 1:
		dil_matrix(a, i, column, b)
	minus_matrix(a, column, i, b)
	print(a)
	print(b)
print(find_result(a,b,rows))
'''
while True:
	
	n = input("Enter do: ")
	k = int(input("Eneter the column: "))
		
	if n == "minus":
		a, b = minus_matrix(a, column, k, b)
	elif n == "dil":
		a, b = dil_matrix(a, k, column, b)
	elif n == "change":
		change_place(a, k, column, chek_matrix(a, rows, k)+k, b)
	elif n == "plus":
		plus_matrix(a, column, k, b)
	elif n == "end":
		print(find_result(a,b,rows))
		break
	elif n == "chek":
		if chek_matrix(a, rows, k)+k:
			print("True")
		else:
			print("False")

	print(b)
	print(a)


#b = a.func()
#c = [[5,4,3,2], [4,3,6,5], [6,6,4,4]]
#d = chek_matrix(c, rows, 0, 1)
#print(c[d][0])
#print(c)
#print(change_place(c, 2, column, 0))

#for i in range(rows):
#	if i+2 != rows:

#потрібен додатковий масив який буде виконувати роль
#уявного рядка при додаванні відніманні і ділені  ------ це всьо фігня, навіть не потрібно таке

'''
