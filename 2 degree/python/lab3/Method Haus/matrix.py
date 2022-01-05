from func import create_matrix, minus_matrix, chek_matrix, change_place, dil_matrix, find_result


rows = int(input("Enter rows matrix: "))
column = int(input("Enter column matrix: "))
if rows != column:
	print("matrix not square!")

a = []
b = []

a, b = create_matrix(rows)

print("Your matrix: ")
print(a)
print(b)

print("******Gauss Method******")
print("*********magic**********")
print("result: ")

for i in range(rows-1):
	if chek_matrix(a, rows, i):
		change_place(a, i, column, chek_matrix(a, rows, i), b)
	if a[i][i] != 1:
		dil_matrix(a, i, column, b)
	minus_matrix(a, column, i, b)
	#print(a)
	#print(b)

result = find_result(a,b,rows)
result.reverse()
for i in range(rows):
	print("x",i, "= ", result[i])
