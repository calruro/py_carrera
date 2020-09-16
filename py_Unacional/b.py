# import a
# print("b", end='')

# class A:
#     pass
    
# class B(A):
#     pass

# class C(B):
#     pass

# print(issubclass(A, C))

# def I(n):
#     s = '+'
#     for i in range(n):
#         s += s
#         yield s

# for x in I(2):
#     print(x, end='')

# class A:
#     def __init__(self, v):
#         self.__a = v + 1

# a = A(0)
# print(a.__a)

# def o (p):
#     def q():
#         return '*' * p
#     return q

# r = o(1)
# s = o(2)
# print(r() + s())

# class A:
#     def __init__(self, v=2):
#         self.v = v
    
#     def set (self, v=1):
#         self.v += v
#         return self.v

# a = A()
# b = a
# b.set()
# print(a.v)

# class A:
#     def __init__(self):
#         pass
#     def f(self):
#         return 1
#     def g():
#         return self.f()

# a = A()
# print(a.g())

# ls = [[c for c in range(r)]for r in range(3)]
# for x in ls:
#     if len(x) < 2:
#         print("["+"]")

# d = {}
# d['2'] = [1, 2]
# d['1'] = [3, 4]

# for x in d.keys():
#     print(d[x][1], end="")

# def f(par2, par1):
#     return par2 + par1

# print(f(1, 2))

# x,y,z = 3,2,1
# z,y,x = x,y,z
# print(x,y,z)

# v = 1 + 1 // 2 + 1 / 2 + 2
# print(v)

# class A:
#     A = 1
#     def __init__(self):
#         self.a = 0

# print(hasattr(A, 'A'))

# class Class:
#     def __init__(self):
#         pass

# def fun(x):
#     return 1 if x % 2 != 0 else 2

# print(fun(fun(1)))

# t = (1,2,3,4)
# t = t[-2:-1]
# t = t[-1]
# print(t)

d = {'one':1, 'three':3, 'two':2}

for k in sorted(d.values()):
    print(k,end=' ')