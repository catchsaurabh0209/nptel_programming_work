# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 00:19:30 2019

@author: OCEAN
"""

with open("file.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("helo world")
myfile.close()   