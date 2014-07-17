'''
Created on 17 Jul 2014

@author: dulshani
'''

def solve():
    pass
    
def main():
    s = raw_input()
    t = raw_input()
    sw = list(s)
    tw = list(s)
    order = True
    
    for char in t:
        if char in sw:
            if char not in tw:
                order = False
            else:
                tw = tw[(tw.index(char)+1):]  
            sw.remove(char)
        else:
            #tree
            print "need tree"
            exit()  
              
    if not sw:
        #array
        print "array"
    elif order == True:
        #automaton
        print "automaton"
    else:
        #both
        print "both"

    
if __name__ == '__main__':
    main()