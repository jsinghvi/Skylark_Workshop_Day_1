#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:54:34 2017

@author: root
"""
import random
choice='y'
score=0
while choice=='y' or choice=='Y':
    n = int(input("Enter your guess from 0 to 9 : "))

    x = round(random.random()*10)

    if n==x:
        print("Good guess!")
        score=score+1
        choice = 'y'

    else:
            print("Oops! tough luck!")
            print("the number was %d"%(x))
            print("Your score is %d"%(score))
            break
