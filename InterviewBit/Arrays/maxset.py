# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 21:21:55 2016

@author: DULEE
"""

def maxset(A):
    result = []
    subArr = []
    max_sum = 0
    max_len = 0    
    for index, num in enumerate(A):
        if num >= 0:
            subArr.append(num)
        if index==len(A)-1 or num<0:
            if subArr:            
                if sum(subArr) > max_sum:                
                    max_sum = sum(subArr)                    
                    max_len = len(subArr)
                    result = subArr
                elif sum(subArr) == max_sum:
                    if len(subArr) > max_len:
                        max_len = len(subArr)
                        result = subArr
                    elif len(subArr) == max_len:
                        if subArr[0] < result[0]:
                            result = subArr
            if num<0 and index!=len(A)-1:
                subArr = []        
    return result
        
print maxset([1, 2, 5, -7, 2, 3])
print maxset([1, 2, 5, -7, 5, 3])
print maxset([2, 3, 3, -7, 1, 2, 5])
print maxset([2, 3, 3, -7, 1, 2, 5, -5])
print maxset([-1, -2, -5, -7, -2])