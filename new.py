# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 21:21:23 2019

@author: OCEAN
"""

import numpy as np
a = np.array([[0, 1, 0], [1, 0, 1]])
print(a)
a += 3
print(a)
b = a + 3
print(b)
print (a[1,2] + b[1,2])