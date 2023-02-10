a = ["Apple", "Orange"]
b = ["Apple", "Orange"]
z=a
print(z is a)
print(z is b)
print(a is b)
b = a
print(a is b)
if "Banana" in a:
    print("Yes")
else:
    print("No")