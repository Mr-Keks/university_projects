#Метод Лагранжа

def l_func(x, ox, k):
	res = 1
	for i in x:
		if i == x[k]:
			continue
		else:
			res = (ox - i) * res
	return res 
def filling_array(k):
	x = []
	for i in range(k):
		x.append(float(input(f"Enret {i} value: ")))
	return x

l = []

r = 5
print("*****Filling array x: ")
x = filling_array(r)
print("\n*****Filling array y: ")
y = filling_array(r)
ox = float(input("\nEnter argument: "))
print()
for i in range(5):
	l.append(l_func(x, ox, i) / l_func(x, x[i], i))
res = 0
for i in range(len(l)):
	res += l[i] * y[i]

print("result = ", res)
