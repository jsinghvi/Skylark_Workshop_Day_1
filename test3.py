#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 12:40:56 2017

@author: root
"""

op = raw_input("Enter operation : ")
a = int(raw_input("Enter first number : "))
b = int(raw_input("Enter second number : "))

if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
elif op=='/':
    print(a/b)
elif op=='%':
    print(a%b)
else:
    print("Wrong operator!")