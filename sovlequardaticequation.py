import cmath
a=float(input("Enter value of A:"))
b=float(input("Enter value of B:"))
c=float(input("Enter value of C:"))

d = (b**2) - (4*a*c)

sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The Solution is :",sol1,sol2)
