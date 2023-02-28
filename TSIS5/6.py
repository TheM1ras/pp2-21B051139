import re

txt = str(input())

x = re.sub(" ", ":", txt)
y = re.sub("[.]", ":", x)
z = re.sub(",", ":", y)

print(z)