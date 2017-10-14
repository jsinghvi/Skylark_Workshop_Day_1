#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:14:25 2017

@author: root
"""

n = int(input("Enter a number : "))

d = n
num=0
while n>0:
    rem = n%10
    num = (num*10) + rem
    n = n/10
if d==num:
    print("It is a palindrome number!")
else:
    print("It is not a palindrome number! :(")