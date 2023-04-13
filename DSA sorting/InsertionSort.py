# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:33:37 2022

@author: aa
"""

def InsertionSort(array,start,end):
    for i in range((start+1),end+1):
        key=array[i]
        j=i-1
        if start == 0:
            while key<array[j] and j>=0 :
                array[j+1]=array[j]
                j=j-1
            array[j+1]=key
        else:
            while key<array[j] and j>0 :
                array[j+1]=array[j]
                j=j-1
            array[j+1]=key
