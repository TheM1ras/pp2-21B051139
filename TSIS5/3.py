import re

txt = str(input())
x= re.findall("[a-z]_[a-z]", txt)
if x:
    print("True")
else:
    print("False")