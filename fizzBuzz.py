# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 22:15:42 2019

@author: OCEAN
"""
print("welcome to fizz buzz game")
n=int(input())
for i in range(1,n+1):
    if(i%3==0 and i%5==0):
        print(i,"fizzbuzz")
    elif(i%3==0):
        print(i,"fizz")
    elif(i%5==0):
        print(i,"buzz")
    else:
        print(i)