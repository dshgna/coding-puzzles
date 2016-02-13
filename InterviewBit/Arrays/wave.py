# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 15:46:28 2016

@author: DULEE
"""

def wave(A):
    x = sorted(A)
    n = len(A)
    for i in range(0,n,2):
        if i+1<n:        
            x[i], x[i+1] = x[i+1], x[i]
    return x
    
print wave([1, 2, 3, 4, 5])