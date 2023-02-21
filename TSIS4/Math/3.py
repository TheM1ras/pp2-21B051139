import math

n = int(input("Number of sides: "))
l = int(input("length of sides: "))

S = float
S = (n*(l**2))/(4*math.tan(math.pi/n))

print(S)