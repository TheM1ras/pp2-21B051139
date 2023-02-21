def gen_even(a):
    for i in range(a):
        if i%2==0:
            yield i
        else:
            continue
        
n = int(input())
for b in gen_even(n):
    print(b)