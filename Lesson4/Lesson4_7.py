def fibo_gen(n):
    a=1
    for i in range(1,n+1):
        a*=i
    yield a

for n in range(1,16):
    for el in fibo_gen(n):
        print(el)