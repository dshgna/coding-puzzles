# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 12:36:14 2016

@author: DULEE
"""

def coverPoints(X, Y):
    #for all points compare with prev point
    A = zip(X, Y)
    total = 0
    for index, item in enumerate(A):        
        if index < len(A)-1:
            curr = item
            after = A[index+1]
            x_dist = abs(curr[0]-after[0])
            y_dist = abs(curr[1]-after[1])            
            # if vertical or horizontal can directly move
            #if diagonal move is possible then x_dist==y_dist
            #else move min(x,y) diagonally then remaining vert/horizon
            #dist = diag + max(x,y)-diag = max(x,y)
            dist = max(x_dist, y_dist)
            total += dist
    return total
    
print coverPoints(
    [ -5, 7, -12, 4, -6, 2, -5, -12, -6, 3, 11, 10, -8, 11, -13, -8, 5, -12, 4, 4 ], 
    [ -6, 6, -8, -13, -2, -9, -10, -10, -7, -14, 9, -8, -4, 8, 13, -11, 13, 5, 9, 11 ])