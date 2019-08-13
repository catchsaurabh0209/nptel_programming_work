# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 16:29:47 2019

@author: OCEAN
"""

def getTotalX(a, b):
    a.sort()
    b.sort()
    c=[]
    
    number=0
    
    for i in range(a[-1],b[0]+1):
        count1=0
        for j in a:
            if(i%j==0):
                count1+=1
        if(count1==len(a)):
            c.append(i)
            
    print(a,b,c)        
    for i in c:
        count=0
        for j in b:
            if j%i==0:
                count+=1
        if(count==len(b)):
            number+=1
    print(number)        
    
getTotalX([3,4],[24,48,96])
    