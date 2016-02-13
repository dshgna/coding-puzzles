# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 14:48:03 2016

@author: DULEE
"""

class Solution:
    # @param a : list of integers
    # @param b : integer
    # @return a list of integers
    def rotateArray(self, a, b):
        ret = []
        if b>len(a):
            b = b % len(a) 
        for i in xrange(len(a)):                 
            ret.append(a[(i + b)%len(a)])
        return ret

s = Solution()

A = [14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35]
B = 56

print s.rotateArray(A, B)