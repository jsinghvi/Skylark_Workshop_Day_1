#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 06:49:23 2017

@author: root
"""

a = int(input("Enter first number : "))
b = int(input("Enter second number : "))
c = int(input("Enter third number : "))

if a>b and a>c:
    max=a
elif b>a and b>c:
    max=b
else:
    max=c

print(max),
