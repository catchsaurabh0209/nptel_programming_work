# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:04:13 2019

@author: OCEAN
"""
import random
with open("dna.txt") as myfile:
    #print(myfile.read())
    #x=myfile.read()
    n=list(myfile.read())
    print(n)
for i in range(0,10):
    m=random.randint(0,len(n)-1)
    p=random.randint(1,100) 
    print(m,p)
    if p==1:
        n[m]=1
    else:
        n[m]=0
print(n)        


'''
it is not a good but important thing is read and write of the file