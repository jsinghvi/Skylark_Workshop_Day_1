# -*- coding: utf-8 -*-

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

a = a if a>b else b
a = a if a>c else c

print(a)


