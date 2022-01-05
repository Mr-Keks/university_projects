import function 


x = 8.1249
dx1 = 8
dx2 = 10**-3
dx = dx1 * dx2


#n = function.approximation(x, dx, len(str(x)))

s = function.ablosute(dx, 5*dx2)

k, pov = function.power(dx1, dx2)

print(k, pov)


a, b = function.truenumber(str(x), pov, s)
f = function.falsenumber(str(x), b)

print("number = ", x)
print("False number = ", f)
print("True number = ", a)
#print(function.istruenumber(str(x), pov, k, b))
print(function.istruenumber(s))