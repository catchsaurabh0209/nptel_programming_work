# -*- coding: utf-8 -*-
"""
Created on Thu Apr 25 23:41:54 2019

@author: OCEAN
"""

import string
dict ={}
data=""

#This file, "Messed_text.txt", will be created by this code itself.
messed=open("Messed_text.txt","w")

for i in range(len(string.ascii_letters)):
    """
    We are generating a Dictonary 'dict'
    Below logic will wrap around the contents of string.ascii_letters
    We know that we have positive and negative indexes for lists and strings.
    Index Shifting happens like this because of [i-13], 0-13=-13 and 52-13=39
    string.ascii_letters[i] is Generating "Keys" and,
    string.ascii_letters[i-13] is Generating "Values" after shifting.
    """
    dict[string.ascii_letters[i]]=string.ascii_letters[i-13]

#If you want to see the dictionary used for conversion, uncomment below print comment.
#print(dict)
"""
We are opening below file and reading, to convert its text.
Make sure both, "Substitution_Cipher.py" and "Plain_text.txt",
files are in same folder.
"""
with open("text.txt") as f:
    while True:
        c=f.read(1)
        #If End Of File (EOF), is reached, program should Stop.
        if not c:
            print("Reached EOF.")
            break
        #Below condition is checking if c is in dict or not.
        if c in dict:
            data=dict[c]
        else:
            """
            If c is not in the dict, then it will be copied as-it-is to
            data. This applies to anything other than Alphabets.
            For example... Numbers, special chars etc.
            """
            data=c
        messed.write(data)
messed.close()