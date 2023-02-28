import re

txt = str(input())
x= re.findall("^[A-Z]{1}[a-z]", txt)
if x:
    print("True")
else:
    print("False")