def div(m):
    def gen_division(a):
      for i in range(a):
        if i%3==0 and i%4==0:
            yield i
        else:
            continue
    return gen_division(m)
n = int(input())
for a in div(n):
    print(a, "", end="")
