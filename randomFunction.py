# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 20:46:13 2019

@author: OCEAN
"""
import random
n=list(range(1,11))
print(n)
m=random.randint(1,5)
#this randint function returns the no. from 1<=m<=5
# this randrange return the no from 1 to 4 only[as per rule of range]
a=random.randrange(1,3)
#choice will return the no from list
b=random.choice(n)
#random returns the decimal no between 0 and 1
c=random.random()
d=random.randrange(1,11,2)
print(m,a,b,c,d)