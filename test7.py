#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 14:32:05 2017

@author: root
"""

n = int(input("Enter the size : "))

for i in range(0,n):
    for j in range(0,i+1):
        print("*"),
        #j=j+1
    print
    #i=i+1