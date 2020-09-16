# print("c", end='')
# import a
# import b

# print(__name__)

# print(len((1, )))

# print("a", "b", "c", sep="'")

# class A:
#     def __init__(self, name):
#         self.name = name

# a = A("class")
# print(a)

# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass

# print(issubclass(C, A) and issubclass(C,B))

# def a(x):
#     def b():
#         return x + x
#     return b

# x = a('x')
# y = a('')
# print(x() + y())

# print(len([i for i in range(0, -2)]))

# z = 2
# y = 1
# x = y < z or z > y and y > z or z < y
# print(x)

# class X:
#     pass

# class Y(X):
#     pass

# class Z(Y):
#     pass

# x = X()
# z = Z()
# print(isinstance(x, Z), isinstance(z, X))

# str1 = 'string'
# str2 = str1[:]

# print(str1, str2)

# i = 4

# while i > 0:
#     i -= 2
#     print("*")
#     if i == 2:
#         break
# else:
#     print("*")

# def I(n):
#     s = ''
#     for i in range(n):
#         s += '*'
#         yield s

# for x in I(3):
#     print(x, end='')

# class A:
#     def __init__(self, v):
#         self._a = v + 1

# a = A(0)
# print(a._a)

# x = 16
# while x > 0:
#     print('*', end='')
#     x //= 2

# x = """
# """
# print(len(x))

# str = 'abcdef'
# def fun(s):
#     del s[2]
#     return s

# print(fun(str))

a = True
b = False
a = a or b
b = a and b
a = a or b
print(a, b)