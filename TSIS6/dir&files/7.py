import os
f = open("/Users/admin/Desktop/KBTU/PP2/Tsis/TSIS6/dir&files/Test.txt", "r")
fc = open("/Users/admin/Desktop/KBTU/PP2/Tsis/TSIS6/dir&files/Test2.txt", "w")
for i in f:
    fc.write(i)
f.close
fc.close
fc = open("/Users/admin/Desktop/KBTU/PP2/Tsis/TSIS6/dir&files/Test2.txt", "r")
print(fc.read())