# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


"""some math programming"""
"""this code tests whether the multiplication of a numbers factors is uniqu"""
import operator
import functools





"""this multiplies all the factors of a number together"""
def factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
        array = list(result)
        newarray = functools.reduce(operator.mul,array, 1)    
    return newarray
    
"""this makes an array of numbers  with their factors multiplied"""    
def answer(n):
    newlist=[]
    for i in range (1,n):
        vari = factors(i)
        newlist.append(vari)
    return newlist
"""this uses the previous array and tells overlap if their is any"""
def answer2(n):
    helparray = answer(n)
    """donearray = [j for j in helparray if helparray[j]>1]
    return donearray"""
    seen = set()
    repeat = set()
    for n in helparray:
        global seen
        if n in seen :
            print("duplicate:", n)
            repeat.add(n)
        else:
            
            seen.add(n)
    return repeat
     
    
    
       
            
