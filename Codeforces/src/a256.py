'''
Created on 17 Jul 2014

@author: dulshani
'''
import math
    
def main():
    a1, a2, a3 = map(int, raw_input().split())
    b1, b2, b3 = map(int, raw_input().split())
    n = int(raw_input())
    min_shelves = math.ceil((a1+a2+a3)/5.0) + math.ceil((b1+b2+b3)/10.0)
    #print min_shelves
    #print n
    if min_shelves<=n:
        print "YES"
    else:
        print "NO"
    
if __name__ == '__main__':
    main()