def zn(s):
	l = len(s)
	res = ""
	chek = 0
	for i in s:
		if i == '.':
			continue
		if i != '0':
			chek = 1
		if chek == 1:
			res+=i
	return res

def point(d, s, k):
	z = ""
	chek=0
	if s[0] == '0':
		z = "0."
		chek = 1
	i = 0
	
	while i < k:
		if s[i] == '.' and chek == 0:
			z+='.'
			i -= 1 
			chek = 1
		else:
			z+=d[i]
		i+=1
	return z

def point2(d, k):
	z = ""
	for i in range(k):
		z+=d[i]
	return z

#print(point(zn("1.0023"), "1.0023", 3))
#print(point2(zn("112321"),2))

print(point(zn("11.45"), "11.45", 3))
