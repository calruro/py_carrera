# # Caesar cipher
# text = input("Enter your message: ")
# cipher = ''
# for char in text:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) + 1
#     if code > ord('Z'):
#         code = ord('A')
#     cipher += chr(code)

# print(cipher)

# # Caesar cipher - decrypting a message
# cipher = input('Enter your cryptogram: ')
# text = ''
# for char in cipher:
#     if not char.isalpha():
#         continue
#     char = char.upper()
#     code = ord(char) - 1
#     if code < ord('A'):
#         code = ord('Z')
#     text += chr(code)

# print(text)

# # Numbers Processor

# line = input("Enter a line of numbers - separate them with spaces: ")
# strings = line.split()
# total = 0
# try:
#     for substr in strings:
#         total += float(substr)
#     print("The total is:", total)
# except:
#     print(substr, "is not a number.")

# # IBAN Validator

# iban = input("Enter IBAN, please: ")
# iban = iban.replace(' ','')
# if not iban.isalnum():
#     print("You have entered invalid characters.")
# elif len(iban) < 15:
#     print("IBAN entered is too short.")
# elif len(iban) > 31:
#     print("IBAN entered is too long.")
# else:
#     iban = (iban[4:] + iban[0:4]).upper()
#     iban2 = ''
#     for ch in iban:
#         if ch.isdigit():
#             iban2 += ch
#         else:
#             iban2 += str(10 + ord(ch) - ord('A'))
#     ibann = int(iban2)
#     if ibann % 97 == 1:
#         print("IBAN entered is valid.")
#     else:
#         print("IBAN entered is invalid.")

# print(float("1, 3"))

# print(3 * 'abc' + 'xyz')

# print('Mike' > 'Mikey')

# print(ord('c') - ord('a'))

# var = 0
# print(assert var == 0)

# x = '\''
# print(len(x))

#print(chr(ord('z')-2))

# class Fib:
#     	def __init__(self, n_n):
# 		self.__n = n_n
# 		self.__i = 0
# 		self.__p1 = self.__p2 = 1

# 	def __iter__(self):
# 		print("Fib iter")
# 		return self

# 	def __next__(self):
# 		self.__i += 1
# 		if self.__i > self.__n:
# 			raise StopIteration
# 		if self.__i in [1, 2]:
# 			return 1
# 		ret = self.__p1 + self.__p2
# 		self.__p1, self.__p2 = self.__p2, ret
# 		return ret

# class Class:
# 	def __init__(self, n):
# 		self.__iter = Fib(n)

# 	def __iter__(self):
# 		print("Class iter")
# 		return self.__iter;

# object = Class(8)

# for i in object:
# 	print(i)

# def Fib(n):
#     p = pp = 1
#     for i in range(n):
#         if i in [0, 1]:
#             yield 1
#         else:
#             n = p + pp
#             pp, p = p, n
#             yield n

# fibs = list(Fib(10))

# print(fibs)

# def I():
#     s = 'abcdef'
#     for c in s[::2]:
#         yield c
# for x in I():
#     print(x, end='')

# class A:
#     def __init__(self, v = 1):
#         self.v = v
    
#     def set(self,v):
#         self.v = v
#         return v

# a = A()
# print(a.set(a.v + 1))    

# class A:
#     def __init__(self, v):
#         self.__a = v + 1

# a = A(0)
# print(a.__a) 

# class A:
#     def __init__(self):
#         self.a = 1
    
# class B:
#     def __init__(self):
#         A.__init__(self)
#         self.b = 2

# def o(p):
#     def q():
#         return '*' * p
#     return q

# r = o(1)
# s = o(2)
# print(r() + s())

# class A:
#     def __str__(self):
#         return 'a'
    
# class B(A):
#     def __str__(self):
#         return 'b'

# class C(B):
#     pass

# o = C()
# print(o)

# class A:
#     X = 0
#     def __init__(self, v = 0):
#         self.Y = v
#         A.X += v
    
# a = A()
# b = A(1)
# c = A(2)
# print(c.X)

# class A:
#     pass
    
# class B(A):
#     pass

# class C(B):
#     pass

# print(issubclass(C,A))

# class I:
#     def __init__(self):
#         self.s = 'abc'
#         self.i = 0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.i == len(self.s):
#             raise StopIteration
#         v = self.s = [self.i]
#         self.i += 1
#         return v

# for x in I():
#     print(x, end='')

# class A:
#     A = 1
#     def __init__(self):
#         self.a = 0

# print(hasattr(A, 'a'))

# assert var != 0

# for x in open('file','rt'):
#     print(x)

# try:
#     raise Exception(1, 2, 3)
# except Exception as e:
#     print(len(e.args))

# print(chr(ord('p')+2))

# print(float("1.3"))

# class A:
#     def a(self):
#         print('a')
    
# class B:
#     def a(self):
#         print('b')

# class C(B, A):
#     def c(self):
#         self.a()

# o = C()
# o.c()

# class I:
#     def __init__ (self):
#         self.s('a')
    
# class B:
#     def a(self):
#         print('b')

# class C(B, A):
#     def c(self):
#         self.a()

# o = C()
# o.c()

import math
print(dir(math))
