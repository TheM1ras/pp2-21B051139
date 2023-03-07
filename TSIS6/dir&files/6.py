import os
abc = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for i in abc:
    fname = "/Users/admin/Desktop/KBTU/PP2/Tsis/TSIS6/dir&files/" + i + ".txt"
    f = open(fname, "x")
    f.close