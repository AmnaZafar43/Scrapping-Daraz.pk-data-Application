# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def bubbleSort( theSeq ):
    n = len( theSeq )
    for i in range( n - 1 ) :
        for j in range(n - 1) :            
            if theSeq[j] > theSeq[j + 1] : 
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
    return theSeq
