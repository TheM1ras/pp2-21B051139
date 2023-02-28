import re


txt = str(input())

x = re.sub("_([a-z])", " \\1", txt)
x = re.split(" ", x)
for i in x:
    print(i.capitalize(), end="")