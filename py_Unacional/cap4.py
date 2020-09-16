# def hiEverybody(myList):
#     for name in myList:
#         print("Hi,", name)

# hiEverybody(["Adam", "John", "Lucy"])

# def listUpdater(lst):
#     updList = []
#     for elem in lst:
#         elem **= 2
#         updList.append(elem)
#     return updList

# l = [1, 2, 3, 4, 5]
# print(listUpdater(l))

# # Example 1
# t1 = (1, 2, 3)
# for elem in t1:
#     print(elem)

# # Example 2
# t2 = (1, 2, 3, 4)
# print(5 in t2)
# print(5 not in t2)

# # Example 3
# t3 = (1, 2, 3, 5)
# print(len(t3))

# # Example 4
# t4 = t1 + t2
# t5 = t3 * 2

# print(t4)
# print(t5)

# def fun(in=2, out=3):
#     return in * out

# print(fun(3))

# tup = (1, ) + (1, )
# tup = tup + tup
# print(len(tup))


# def fun(x):
#     global y
#     y = x * x
#     return y

# fun(2)
# print(y)

# dct = {'one':'two', 'three': 'one', 'two':'three'}
# v = dct['one']
# for k in range (len(dct)):
#     v = dct[v]
# print (v)

# def fun(x):
#     x += 1
#     return x

# x = 2
# x = fun(x + 1)
# print(x)

# def f(x):
#     if x == 0:
#         return 0
#     return x + f(x-1)

# print(f(3))

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return
        
# print(fun(fun(2))+1)

# def any():
#     print(var+ 1, end='')
# var = 1
# any()
# print(var)

# tup = (1,2,4,8)
# tup = tup[1:-1]
# tup = tup[0]
# print(tup)

# def fun(inp=2, out=3):
#     return inp * out

# print(fun(out=2))

# dct = {}
# lst = ['a', 'b', 'c', 'd']
# for i in range(len(lst)-1):
#     dct[lst[i]] = (lst[i],)
# for i in sorted(dct.keys()):
#     k = dct[i]
#     print(k[0])

# def func(a, b):
#     return a ** a

# print(func(2))

# list = ['Mary', 'had', 'a', 'little', 'lamb']
# def list(lst):
#     del lst[3]
#     lst[3] = 'ram'
# print(list(list))

# def func1(a):
#     return a ** a
# def func2(a):
#     return func1(a) * func1(a)

# print(func2(2))

# def fun(x,y,z):
#     return x+2*y+3*z

# print(fun(0, z= 1, y = 3))

# i = 0
# while i < i + 2:
#     i += 1
#     print("*")
# else:
#     print("*")

# dd = {"1":"0", "0":"1"}
# for x in dd.vals():
#     print(x, end="")

# x = float(input())
# y = float(input())
# print(y ** (1 / x))

# y = input()
# x = input()
# print(x + y)

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return 2
        
# print(fun(fun(2)))

# dct = {'one':'two', 'three':'one', 'two':'three'}
# v = dct['three']

# for k in range(len(dct)):
#     v = dct[v]

# print(v)

# dct = {}
# dct['1'] = (1,2)
# dct['2'] = (2,1)

# for x in dct.keys():
#     print(dct[x][1], end="")

# x= int(input())
# y= int(input())
# x = x % y
# x = x % y
# y = y % x
# print(y)

# y = 1 // 2
# print(y)

# def fun(a, b, c = 0):
#     print(a,b,c)

# tup = (1,2,4,8)
# tup = tup[-2:-1]
# tup = tup[-1]
# print(tup)

# def fun(inp=2, out=3):
#     return inp * out    
# print(fun(out=2))

# a = 1
# b = 0
# a = a ^ b
# b = a ^ b
# a = a ^ b

# print(a, b)

# x = 1 // 5 + 1 / 5
# print(x)

# x = 1
# y = 2
# x, y, z = x, x, y
# z, y, z = x, y, z

# print(x,y,z)

# z=0
# y=10
# x=y < z and z > y or y > z and z < y
# print(x)

# lst=[1,2]

# for v in range(2):
#     lst.insert(-1, lst[v])

# print(lst)

# lst = [i for i in range(-1,-2)]
# print(lst)

# def func1(a):
#     return None

# def func2(a):
#     return func1(a)*func1(a)

# print(func2(2))

lst = [[x for x in range(3)] for y in range(3)]

for r in range(3):
    for c in range(3):
        if lst[r][c]%2 != 0:
            print("#")