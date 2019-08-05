# -*- coding: utf-8 -*-
"""
Created on Mon Aug 05 10:09:04 2019

@author: Vicente
"""

import scipy as sp
import matplotlib.pylab as plt
import sys
import numpy
lista=[]
a1=random.random()
print a1
lista.append(a1)
a2=random.random()
print a2
lista.append(a2)
b=random.uniform(0,1,2)
for i in b:
    print i
    lista.append(i)
c1= numpy.random.uniform(0,1)
print c1
lista.append(c1)
c2= numpy.random.uniform(0,1)
print c2
lista.append(c2)
d=numpy.random.uniform(0,1,size=(2,1))
print d
for i in d:
    for j in i:
        print j
        h=len(str(j))-1
        print h
        lista.append(j)
print lista        
        
