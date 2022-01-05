#function for task 2

def approximation(x, dx,v):
return float(f'{x / (1 + dx):.{v}f}')

def ablosute (x, y):
	return x < y

def power(dx1, dx2):
	chek = 0
	count = 0
	if dx1 == 0:
		dx = str(dx1 * dx2)

		for i in dx:
			if i == '.':
				chek = 1
				continue
			if i != '0' and chek == 1:
				n = i
				break
			elif i == '0' and chek == 1:
				count += 1
	else:
		dx = str(dx1 * dx2)
		for i in dx:
			if i == '.':
				chek = 1
				continue
			if i != '0' and chek == 1:
				n = i
				break
			elif i == '0' and chek == 1:
				count += 1

	return float(f'{int(n) * 10**-count:.{count}f}'), count

def truenumber(num, n, tn):
	chek = 0
	s = 0
	k = 1
	a = []
	for i in num:
		if i != '.':
			n+=1
		else:
			break
	if tn == False:
		return "no true numbers", n
	for i in num:
		if k == n+1:
			break
		if i == '.':
			continue
		if i == '0' and k != n and chek == 0 and num[k+1] != 0:
			chek = 1
		if k <= n and (i != '0' or chek == 1):
			a.append(i)
	
		k += 1
	return a, n

def falsenumber(num,n):
	b = []
	chek = 0
	k = 0
	for i in num:
		if i == '.':
			continue
		k += 1
		if k > n and i != '.':
			b.append(i)
	return b
'''
def istruenumber(num, n, s, k):
	if float(s) < 5*10**-n:
		print("number ", num[k], " is true")
	else:
		print("number ", num[k], "is false")

	return " "
'''
def istruenumber(n):
	if n:
		return "true"
	else:
		return "false"