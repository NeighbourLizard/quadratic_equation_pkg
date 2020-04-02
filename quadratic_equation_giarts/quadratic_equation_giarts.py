import cmath

# Quadratic function f(x) = (a * x^2) + b*x + c
# 
# Discriminant D = b**2 - 4*a*c

def quadratic_equation_giarts(a,b,c):
	Fx = "{}x^2 + {}*x + {}".format(a,b,c)
	print("f(x) = {}".format(Fx))
	D = (b*b - 4*a*c)

	if D > 0:
		print("Discriminant is more than 0")
		print("Number of roots: 2 ")
		x1 = (((-b) + cmath.sqrt(D))/(2*a))
		x2 = (((-b) - cmath.sqrt(D))/(2*a))
		print("root number 1: {}\n root number 2: {}".format(x1,x2))
		return x1, x2
	elif D == 0:
		print("Discriminant is equal to 0")
		print("Number of roots: 1")
		x1 = x2 = (-b) / (2*a)
		print("root number 1: {}".format(x1))
		return x1, x2
	else:
		print("Discriminant is less than 0")
		print("Please restart the program and try again.")
		x1 = x2 = null
		return x1, x2
	return
