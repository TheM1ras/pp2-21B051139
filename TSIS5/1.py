import re

txt = str(input())
x= re.search("a*b", txt)
if x:
    print("True")
else:
    print("False")