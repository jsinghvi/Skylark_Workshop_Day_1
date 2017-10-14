#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:38:49 2017

@author: root
"""

n = int(input("Enter a number : "))

sum=1

for i in range(1,n):
    sum=sum+(sum*i)

print(sum)