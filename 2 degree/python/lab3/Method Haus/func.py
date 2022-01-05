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
	if res > matrix[the_rows+1][a]:
		a1 = the_rows+1	
	return a1

def change_place(matrix, the_rows, column, change_rows, b):
	temp = 0
	n = the_rows
	while the_rows < column:
		temp = matrix[n][the_rows]
		matrix[n][the_rows] = matrix[change_rows][the_rows]
		matrix[change_rows][the_rows] = temp
		the_rows += 1
	temp = b[n]
	b[n] = b[change_rows]
	b[change_rows] = temp

	return matrix, b

def find_result(a, b, rows):
	k = []
	rows -= 1
	temp = 0
	for i in range(rows, -1, -1):
		res = 0
		c = 0
		for j in range(rows, -1, -1):
			try:
				res += a[i][j] * k[c]
				c+=1
			except IndexError:
				if a[i][j] != 0:
					temp = a[i][j]
				break
		if i == rows:
			k.append(float(f'{(b[i] / temp):.3f}'))
		else:
			k.append(float(f'{((b[i] - res) / temp):.3f}'))

	return k

def create_matrix(rows):
	a = []
	b = []
	for i in range(rows):
		temp = []
		for j in range(rows):
			print("Enter ", i, "rows and ", j, "column element matrix: ", end='')
			temp.append(float(input()))
		print("Enter ", i, "free element: ", end='')
		b.append(float(input()))
		a.append(temp)
	return a, b