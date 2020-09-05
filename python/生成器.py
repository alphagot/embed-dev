# __author:  xiaoxinpro13
# date:  2020/8/18

def foo():
    for x in range(1, 100):
        yield x * x
        print('-----')
    return None


L = (X * X for X in range(100))
print(next(L))
print(next(L))
print(next(L))
print(next(L))

g = foo()

print(next(g))
print(next(g))
print(next(g))
print(next(g))
