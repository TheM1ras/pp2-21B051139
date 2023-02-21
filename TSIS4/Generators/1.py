def gen_square(a):
    for i in range(a): 
        yield i**2
N = int(input())
for b in gen_square(N):
    print(b)