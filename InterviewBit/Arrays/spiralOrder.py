# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 15:32:50 2016

@author: DULEE
"""

def spiralOrder(A):
    result = []
    ## Actual code to populate result       
    max_row = len(A)-1
    max_col = len(A[0])-1
    dir = 0
    while A:
        if dir== 0: #from left to right        
            for x in A[0]:
                result.append(x)
            A = A[1:]
            max_row -= 1
        #from top to bottom
        elif dir==1:
            for x in A:             
                result.append(x[max_col] )
                del x[max_col]
            max_col -=1
        #from right to left
        elif dir==2:
            for x in A[max_row][::-1]:
                result.append(x)
            A = A[:max_row]
            max_row -= 1
        #from bottom to top
        else:
            for x in A[::-1]:             
                result.append(x[0] )
                del x[0]
                if not x:
                    del x
            max_col -=1
        dir = (dir+1)%4
        A = filter(None, A)
    return result
 
A = [
  [335, 401, 128, 384, 345, 275, 324, 139, 127, 343, 197, 177, 127, 72, 13, 59],
  [102, 75, 151, 22, 291, 249, 380, 151, 85, 217, 246, 241, 204, 197, 227, 96],
  [261, 163, 109, 372, 238, 98, 273, 20, 233, 138, 40, 246, 163, 191, 109, 237],
  [179, 213, 214, 9, 309, 210, 319, 68, 400, 198, 323, 135, 14, 141, 15, 168]
]

print spiralOrder(A)