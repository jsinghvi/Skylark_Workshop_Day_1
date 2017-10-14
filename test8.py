#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 15:03:17 2017

@author: root
"""

import random
r = round(random.random()*100)
if r%2==0:
    print("%d is even"%(r))
else:
    print("%d is odd"%(r))