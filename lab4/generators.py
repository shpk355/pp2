def squar(p):
    i = 1
    while i<=p:
        yield i**2
        i+=1
# for j in squares(4):
#     print(j)
n = int(input())
def even(n):
    i = 0
    while i<=n:
        yield i
        i+=2
for i in even(n):
    if i < n-1:
        print(i, end=",")
    else:
        print(i)

def it(n):
    i = 0
    while i<=n:
        yield i
        i+=12
for j in it(n):
    print(j)
def squares(a, b):
    i = a
    while i<=b:
        yield i*i
        i+=1
for i in squares(1, n):
    print(i, end=" ")
def gen(n):
    while n>=0:
        yield n
        n-=1
for i in gen(n):
    print(i, end=" ")