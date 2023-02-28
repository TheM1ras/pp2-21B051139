import re

txt = str(input())

x = re.search("^ab{2}|^ab{3}", txt)

if x:
    print("True")
else:
    print("False")