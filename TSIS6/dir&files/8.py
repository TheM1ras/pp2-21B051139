import os
path_dir = "/Users/admin/Desktop/KBTU/PP2/Tsis/TSIS6/dir&files"
if os.path.exists(path_dir):
    print("Yes")
    os.remove(path_dir)
else:
    print("No")