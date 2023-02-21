def square(a, b):
    for i in range(a, b): 
        yield i**2
n = int(input())
m = int(input())
for b in square(n, m):
    print(b)