# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 13:56:31 2015

@author: HansG17
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 00:43:42 2015

@author: HansG17
"""
import math
from fractions import Fraction
"""this will do the first problem for  camp"""
#def tomixedfraction(x,y):
#    first =Fraction(x/y).limit_denominator()
#    
#    print(first)
#    improper = math.floor(x/y)
#    impropers = Fraction(first - improper).limit_denominator()
#    
#    print(str(improper)+" "+str(impropers))
#    print(improper*impropers)
#    finalvar = improper*impropers
#   # print(finalvar.denominator)
#    global finalvar
#    return finalvar
    
    
def untilproper(x,y):
#    first =Fraction(x/y).limit_denominator()
#    
#    print(first)
#    improper = math.floor(x/y)
#    impropers = Fraction(first - improper).limit_denominator()
#    
#    print(str(improper)+" "+str(impropers))
#    print(improper*impropers)
#    finalvar = improper*impropers
    i=0
    while(x>y):
        if i<100:
            first =Fraction(x/y).limit_denominator()
            print(first)
            improper = math.floor(x/y)
            impropers = Fraction(first - improper).limit_denominator()
            print(str(improper)+" "+str(impropers))
            print(improper*impropers)
            finalvar = improper*impropers

            x= finalvar.numerator
            print(x)
            y= finalvar.denominator
            print(y)
            i=i+1
        else:
            print("this probably doesnt converge")
            break
    return
    
    
    
    
#def betterfraction():
#    return simple
#    
#    
#def multipliedfraction():
#    