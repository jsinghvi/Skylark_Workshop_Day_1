#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:20:36 2017

@author: root
"""

n = int(input("Enter a number : "))

for i in range(2,(n/2)+1):
    if n%i==0:
        flag=False
        break;
    else:
        flag=True
if flag is True:
    print("It is a prime number!")
else:
        print("It is not a prime number!")
