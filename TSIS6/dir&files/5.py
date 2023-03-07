import os
f = open("/Users/admin/Desktop/KBTU/PP2/Tsis/TSIS6/dir&files/Test.txt", "a")
rand = ["njoe", "1254", "bdhibcie", "bhdijje"]
for i in rand:
    f.write("\n")
    f.write(i)
f.close
f = open("/Users/admin/Desktop/KBTU/PP2/Tsis/TSIS6/dir&files/Test.txt", "r")
print(f.read())
f.close