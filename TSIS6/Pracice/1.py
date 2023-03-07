import os

def createFile(fname):
    if os.path.exists(fname):
     fname = fname + ".txt"
     f = open(fname, "x")
     print(fname, "has been created")
     f.close
    else:
       print(fname, "does not exist, or wrong file name\nTry again\n")
    pass

def readFile(fname):
    if os.path.exist(fname):
     fname = fname + ".txt"
     f = open(fname, "r")
     print("Contents of", fname, "\n", f.read())
     f.close
    else:
       print(fname, "does not exists, or wrong file name\nTry again\n")
    pass

def appendFile(fname):
    if os.path.exists(fname):
        fname = fname + ".txt"
        f = open(fname, "a",)
        f.write("\n")
        f.write(input("You may start writing:\n"))
        f = open(fname, "r",)
        print(f.read())
        f.close
    else:
       print(fname, "does not exist, or wrong file name\nTry again\n")
    pass

def overwriteFile(fname): 
    if os.path.exists(fname):
        fname = fname + ".txt"   
        f = open(fname, "w")
        f.write(input("You may start writing:\n"))
        f = open(fname, "r")
        print("The file", fname, "insides now are:\n", f.read())
        f.close
    else:
        print(fname, "does not exist, or wrong file name\ntry again\n")
    pass

def removeFile(fname):
    fname = fname + ".txt"
    if os.path.exists(fname):
      os.remove(fname)
      print("You have deleted", fname)
    else:
      print(fname, "does not exist, or wrong file name\nTry again")
    pass


print('Welcome to my blog!\nWhat do you want to do with files/the file?')
option = int(input('Options(type a number):\n1-Create a new file\n2-Read existing file\n3-Update some information in a file\n4-Overwrite all content in a file\n5-Remove existing file\nWrite a number(1-5): '))

file_name = input('Please enter a file name (no extension, .txt will be added automatically):').strip()

if option == 1:
    createFile(file_name)
elif option == 2:
    readFile(file_name)
elif option == 3:
    appendFile(file_name)
elif option == 4:
    overwriteFile(file_name)
elif option == 5:
    removeFile(file_name)