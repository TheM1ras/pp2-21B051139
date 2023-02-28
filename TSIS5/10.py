import re

txt = str(input())

x = re.sub("([A-Z])", " \\1", txt)

x = re.sub(" ", "_", x)

for i in x:
    print(i.lower(), end="")