def reverse(a):
    i = int(0)
    while i <= a: 
        yield a-i
        i+=1
N = int(input())
for b in reverse(N):
    print(b)