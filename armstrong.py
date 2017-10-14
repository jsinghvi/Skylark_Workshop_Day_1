#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:17:40 2017

@author: root
"""
n = int(input("Enter a number : "))
temp = n
ndigits=0
while temp>0:
    ndigits=ndigits+1
    temp=temp/10
d = n
sum=0
while n>0:
    rem = n%10
    sum = sum + (rem**ndigits)
    n = n/10


if sum==d:
    print("It is an armstrong number!")

else:
    print("Not an armstrong number!")