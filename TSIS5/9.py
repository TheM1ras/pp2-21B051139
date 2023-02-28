import re

txt = str(input())

x = re.sub("([A-Z])", " \\1", txt)
x = re.split(" ", x)

for i in x:
    print(i, end=" ")